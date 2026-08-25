from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class User(BaseModel):
    name:str
    age:int
    password:str

class response_user(BaseModel):
    name:str
    age:int

@app.get("/users",response_model=response_user)

def get_user():
    return{
        "name":"sachin",
        "age":26,
        "password":"1234"
    }