from sqlalchemy import Column, Integer, String, func, desc 
from database import Base, SessionLocal


class User(Base):
    __tablename__ = "user"
    __table_args__ = {"schema": "public"}

    age = Column(Integer)
    city = Column(String)
    country = Column(String)
    exp_group = Column(Integer)
    gender = Column(Integer)
    id = Column(Integer, primary_key=True, name="id")
    os = Column(String)
    source = Column(String)


if __name__ == "__main__":
    session = SessionLocal()
    results = (
        session.query(User.country, User.os, func.count(User.id))
        .filter(User.exp_group == 3)
        .group_by(User.country, User.os)
        .having(func.count(User.id) > 100)
        .order_by(desc(func.count(User.id)))
        .all()
    )
    print(results)
    #print('[' + ', '.join([str((x.country, x.os)) for x in results]) + ']')