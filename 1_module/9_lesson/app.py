from fastapi import FastAPI, HTTPException, Depends
# from user import User
from pydantic import BaseModel
import datetime
import psycopg2
import logging
from psycopg2.extras import RealDictCursor


app = FastAPI()


# @app.get('/')
# def return_sum():
#     return 'hello, world'


@app.get('/')
def return_sum(a: int, b: int) -> int:
    return a + b


@app.get('/sum_date')
def sum_date(current_date: datetime.date, offset: int):
    return current_date + datetime.timedelta(days=offset)


def get_db():
    return psycopg2.connect(
        "postgresql://robot-startml-ro:PASSWORD@HOST:6432/startml",
        cursor_factory=RealDictCursor,
    )


@app.get('/user/{id}')
def get_user_data(id: int, db=Depends(get_db)):
    with db.cursor() as cursor:
        cursor.execute(
            """
            SELECT 
                gender, 
                age, 
                city
            FROM "user"
            WHERE id = {0}
            """.format(id)
        )
        result = cursor.fetchall()
    logging.info(result)
    if len(result) > 0:
        return result[0]
    else:
        raise HTTPException(404, 'user not found')


class PostResponse(BaseModel):
    id: int
    text: str
    topic: str

    class Config:
        orm_mode = True


@app.get('/post/{id}', response_model=PostResponse)
def get_post_data(id: int, db=Depends(get_db)) -> PostResponse:
    with db.cursor() as cursor:
        cursor.execute(
            """
            SELECT 
                id, 
                text, 
                topic
            FROM post 
            WHERE id = {0}
            """.format(id)
        )
        result = cursor.fetchall()
    logging.info(result)
    if len(result) > 0:
        return PostResponse(**result[0])
    else:
        raise HTTPException(404, 'post not found')


class User(BaseModel):
    name: str
    surname: str
    age: int
    registration_date: datetime.date


@app.post('/user/validate')
def validate_user(user: User):
    return f'Will add user: {user.name} {user.surname} with age {user.age}'
