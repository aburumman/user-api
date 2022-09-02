import uvicorn
from fastapi import FastAPI, HTTPException
from schemas import UserInput, UserOutput, load_db, save_db


app = FastAPI(title = "User API")

db = load_db()

@app.get("/users/")
def get_users(id: int|None = None, name: str|None = None) -> list:
    ''' Returns a list of user '''
    result = db
    if name:
        result = [user for user in result if user.name == name ]
    if id:
        result = [user for user in result if user.id == id ]

    return result

@app.get("/users/{userId}")
def user_by_id(id: int) -> dict:
    result = [user for user in db if user.id == id]
    if result:
        return result[0]
    else:
        raise HTTPException(status_code=404, details= f"{id} not in car data") 

@app.post("/users/", response_model = UserInput)
def add_user(user: str) -> UserOutput:
    new_user = UserOutput(name=user.name, id=len(db)+1)
    db.append(new_user)
    save_db(db)
    return new_user

#if __name__ == '__main__':
#    uvicorn.run("user_api:app", reload=True)
