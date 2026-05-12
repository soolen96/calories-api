from fastapi import FastAPI

from models.person import Person
from core.config import save_info, show_users

app = FastAPI()

@app.post("/basic-info")
async def save_data(person_info:Person):
    return save_info(person_info) 

@app.get("/users")
async def get_users_data():
    return show_users()