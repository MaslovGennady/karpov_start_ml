import os
import pandas as pd
from sqlalchemy import create_engine
from typing import List
from fastapi import FastAPI, HTTPException, Depends
from schema import PostGet
from datetime import datetime
import psycopg2
from psycopg2.extras import RealDictCursor
from catboost import CatBoostClassifier
import hashlib
from pydantic import BaseModel

USER_BUCKET_SALT = 'USER_BUCKET_SALT'
USER_BUCKETS_NUM = 2

class Response(BaseModel):
    exp_group: str
    recommendations: List[PostGet]

def get_exp_group(user_id: int) -> str:
    
    user_str = str(user_id) + USER_BUCKET_SALT
    hash_object = hashlib.md5(user_str.encode())
    hex_dig = hash_object.hexdigest()
    bucket = int(hex_dig, 16) % USER_BUCKETS_NUM
    
    return 'control' if bucket == 0 else 'test'

def get_model_path(path: str, exp_group: str) -> str:
    if os.environ.get("IS_LMS") == "1":  # проверяем где выполняется код в лмс, или локально. Немного магии
        if exp_group == 'control': 
            MODEL_PATH = '/workdir/user_input/model_control'
        else:
            MODEL_PATH = '/workdir/user_input/model_test'
    else:
        MODEL_PATH = path
    return MODEL_PATH

def load_models():
    model_path = get_model_path("C:/Users/maslo/курсы/karpov_start_ml/4_module/11_lesson/catboost_model_v001", 'control')
    model_control = CatBoostClassifier()
    model_control.load_model(model_path)
    model_path = get_model_path("C:/Users/maslo/курсы/karpov_start_ml/4_module/11_lesson/catboost_model_v002", 'test')
    model_test = CatBoostClassifier()
    model_test.load_model(model_path)
    #print(model.predict)
    return model_control, model_test

def batch_load_sql(query: str) -> pd.DataFrame:
    CHUNKSIZE = 200000
    engine = create_engine(
        "postgresql://robot-startml-ro:PASSWORD@"
        "HOST:6432/startml"
    )
    conn = engine.connect().execution_options(stream_results=True)
    chunks = []
    for chunk_dataframe in pd.read_sql(query, conn, chunksize=CHUNKSIZE):
        chunks.append(chunk_dataframe)
    conn.close()
    return pd.concat(chunks, ignore_index=True)

model_control, model_test = load_models()

posts_data = batch_load_sql('select post_id, text, topic, length(text) as text_len from post_text_df')

user_data_source = batch_load_sql('SELECT user_id, gender, age, country, city, exp_group, os, source FROM user_data')

text_embeddings = batch_load_sql('SELECT post_id,"PC0","PC1","PC2","PC3","PC4","PC5","PC6","PC7","PC8","PC9","PC10","PC11","PC12","PC13","PC14","PC15","PC16","PC17","PC18","PC19" FROM g_maslov_post_text_embeddings')

posts_data_full = posts_data.merge(text_embeddings, 
                                   how='left', 
                                   left_on='post_id',
                                   right_on='post_id').copy()

app = FastAPI()
@app.get("/post/recommendations/", response_model=Response)
def recommended_posts(
		id: int, 
		time: datetime, 
		limit: int = 10) -> Response:
        
    exp_group = get_exp_group(id)
        
    user_data = user_data_source[user_data_source['user_id'] == id].drop('user_id', axis=1)
    pred_data = pd.DataFrame([user_data.values[0]] * len(posts_data), columns=user_data.columns)
    
    if exp_group == 'control':
        pred_data = pd.concat([pred_data, posts_data.drop('text', axis=1)], axis=1)
    else:
        pred_data = pd.concat([pred_data, posts_data_full.drop('text', axis=1)], axis=1)
    
    pred_data['timestamp_dayofweek'] = time.weekday()
    pred_data['timestamp_hour'] = time.hour
    predict = pred_data[['post_id']]
    
    if exp_group == 'control':
        predict['predict'] = model_control.predict_proba(pred_data.drop('post_id', axis=1))[:,1]
    else:
        predict['predict'] = model_test.predict_proba(pred_data.drop('post_id', axis=1))[:,1]
    
    predict = predict.sort_values(by='predict', ascending=False).head(5)['post_id'].values
    result = []
    if len(predict) > 0:
        for post_id in predict:
            post = posts_data[posts_data['post_id'] == post_id]
            res_text = post['text'].values[0]
            res_topic = post['topic'].values[0]
            result.append(PostGet(id=post_id, text=res_text, topic=res_topic))
    else:
        raise HTTPException(404, 'predict not found')
    
    result = Response(exp_group=exp_group, recommendations=result)
    
    return result