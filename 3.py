from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

@app.post("/user")
def post_user(name:str="akhil",age:int=26):
    return {
        "name":name,
        "age":age
    }

# pydentic: 

class users(BaseModel):
    name:"str"
    age:int

@app.post("/user_detail")
def user_det(user:dict):
    return{
        "message":"user created",
        "data":user
    }




