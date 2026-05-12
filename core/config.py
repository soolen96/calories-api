import os
import json
from models.person import Person

json_path = "data/basic-info-people.json"

def save_info(person_info:Person):
    new_user = person_info.model_dump()

    users_list = []

    if os.path.exists(json_path):
        with open(json_path, "r") as file:
            try: 
                users_list = json.load(file)
            except json.JSONDecodeError:
                users_list = []

    users_list.append(new_user)

    with open(json_path,"w") as file:
        json.dump(users_list, file, indent=4)

    return {
        "mensaje":f"perfil de: :{person_info.name} creado y guardado exitosamente"
    }

def show_users():
    with open(json_path, "r") as file:
            try: 
                users_list = json.load(file)
            except json.JSONDecodeError:
                users_list = []
            
    return users_list