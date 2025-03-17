import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://robot-startml-ro:PASSWORD@"
    "HOST:6432/startml"
)

user_data = pd.read_sql('select user_id from user_data', con=engine)
print('Insert started')
user_data.to_sql('g_maslov_user_features_lesson_22', if_exists='replace', con=engine, method='multi') # записываем таблицу

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
    
def load_features() -> pd.DataFrame:
    return batch_load_sql('select * from g_maslov_user_features_lesson_22')
    
#load_features()