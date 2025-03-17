from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import desc, func

from database import SessionLocal
from table_user import User
from table_post import Post
from table_feed import Feed
from schema import UserGet, PostGet, FeedGet

app = FastAPI()


def get_db():
    with SessionLocal() as db:
        return db


@app.get("/user/{id}", response_model=UserGet)
def get_user(id: int, db: Session = Depends(get_db)):
    responce = db.query(User).filter(User.id == id).all()
    if len(responce) > 0:
        return responce[0]
    else:
        raise HTTPException(404, 'user not found')
    

@app.get("/post/{id}", response_model=PostGet)
def get_post(id: int, db: Session = Depends(get_db)):
    responce = db.query(Post).filter(Post.id == id).all()
    if len(responce) > 0:
        return responce[0]
    else:
        raise HTTPException(404, 'post not found')


@app.get("/user/{id}/feed", response_model=List[FeedGet])
def get_user_feed(id: int, limit: int = 10, db: Session = Depends(get_db)):# -> List[FeedGet]:
    responce = db.query(Feed).filter(Feed.user_id == id).order_by(desc(Feed.time)).limit(limit).all()
    if len(responce) > 0:
        return responce
    else:
        raise HTTPException(200, [])
    

@app.get("/post/{id}/feed", response_model=List[FeedGet])
def get_post_feed(id: int, limit: int = 10, db: Session = Depends(get_db)):# -> List[FeedGet]:
    responce = db.query(Feed).filter(Feed.post_id == id).order_by(desc(Feed.time)).limit(limit).all()
    if len(responce) > 0:
        return responce
    else:
        raise HTTPException(200, [])
        
        
@app.get("/post/recommendations/", response_model=List[PostGet])
def get_top_posts(id: int, limit: int = 10, db: Session = Depends(get_db)):# -> List[PostGet]:
    
    top_posts = (db \
                 .query(Feed.post_id) \
                 .filter(Feed.action  == "like") \
                 .group_by(Feed.post_id) \
                 .order_by(desc(func.count(Feed.post_id))) \
                 .limit(limit) \
                ).subquery()
    
    responce = db \
               .query(Post) \
               .join(top_posts, Post.id == top_posts.c.post_id) \
               .all()

    if len(responce) > 0:
        return responce
    else:
        raise HTTPException(200, [])