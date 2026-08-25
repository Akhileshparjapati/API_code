from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
user=[]
class users(BaseModel):
    name:str
    age:int

@app.post("/users")
def user_det(users:users):
    user.append(users)
    return {
        "message":"user created",
        "user":users
    }

@app.put("/users/{user_id}")
def update_det(user_id:int,users:users,notify:bool=False):
    if user_id<len(user):
        user[user_id]=users
        return {
            "message":"user updated",
            "user":users,
            "notify":notify
        }
    return {"message":"user not found"}     