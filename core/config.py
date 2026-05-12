import os
import json
from models.person import Person

def save_info(person_info:Person):
    path = "data/basic-info-people.json"
    new_user = person_info.model_dump()

    users_list = []

    if os.path.exists(path):
        with open(path, "r") as file:
            try: 
                users_list = json.load(file)
            except json.JSONDecodeError:
                users_list = []

    users_list.append(new_user)

    with open(path,"w") as file:
        json.dump(users_list, file, indent=4)

    return {
        "mensaje":f"perfil creado y guardado exitosamente en JSON exitosamente de: :{person_info.name}"
    }
