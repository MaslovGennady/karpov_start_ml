from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, func, desc 
from sqlalchemy.orm import relationship
from database import Base, SessionLocal
from table_post import Post
from table_user import User


class Feed(Base):
    __tablename__ = "feed_action"
    __table_args__ = {"schema": "public"}

    action = Column(String)
    post_id = Column(Integer, ForeignKey(Post.id), primary_key=True)
    post = relationship(Post, foreign_keys=[post_id])
    time = Column(TIMESTAMP)
    user_id = Column(Integer, ForeignKey(User.id), primary_key=True)
    user = relationship(User, foreign_keys=[user_id])