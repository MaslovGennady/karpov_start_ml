from sqlalchemy import Column, Integer, String, desc
from database import Base, SessionLocal


class Post(Base):
    __tablename__ = "post"
    __table_args__ = {"schema": "public"}

    id = Column(Integer, primary_key=True, name="id")
    text = Column(String)
    topic = Column(String)
    
    
if __name__ == "__main__":
    session = SessionLocal()
    results = (
        session.query(Post)
        .filter(Post.topic == "business")
        .order_by(desc(Post.id))
        .limit(10)
    )
    
    print('[' + ', '.join([str(x.id) for x in results]) + ']')