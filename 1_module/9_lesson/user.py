from pydantic import BaseModel
import datetime


class User(BaseModel):
    name: str
    surname: str
    age: int
    registration_date: datetime.date
