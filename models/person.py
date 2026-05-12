from pydantic import BaseModel

class Person(BaseModel):
    name: str
    gender: str
    height: float
    weight: float
    age: int 