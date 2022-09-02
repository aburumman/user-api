import json
from pydantic import BaseModel
 
class UserInput(BaseModel):
  name: str | None

class UserOutput(UserInput):
    id: int  


def load_db() -> list[UserOutput]:
    ''' Will load a list of users '''
    with open("users.json") as f:
        return [UserOutput.parse_obj(obj) for obj in json.load(f)]

def save_db(users: list[UserInput]):
    with open("users.json", 'w') as f:
        json.dump([user.dict() for user in users], f, indent=4)
        

