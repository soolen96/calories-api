import json
import os
from fastapi import FastAPI
from pydantic import BaseModel

from models.person import Person
from core.config import save_info


app = FastAPI()



@app.post("/basic-info")
async def get_info(person_info:Person):
    save_info(person_info)
    
    return person_info.name

