from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class user(BaseModel):
    Name:str
    age:int
    email:str

@app.post("/user_db")

def user_detail(user:user):
    return {
        "message":"user created",
        "user":user

    }


class Address(BaseModel):
    State:str
    country:str

class user_det(BaseModel):
    name:str
    age:int
    addres:Address

@app.post("/user_data")

def user_funct(user_det:user_det):
    return user_det