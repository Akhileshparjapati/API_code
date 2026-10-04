from fastapi import FastAPI, HTTPException,status,exceptions
from pydantic import BaseModel

app=FastAPI()

@app.post("/user",status_code=status.HTTP_201_CREATED)

def create_user():
    return{
        "message":"user created"
    }

@app.get("/user")
def get_user():
    return{
        "request":"success",
        "code":200,
        "data":{
            "name":"AKhile",
            "age":26
        }
    }

@app.get("/user/{user_id}")
def get_user_up(user_id:int):
    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        ) 
    return {
        "id":1,
        "name":"Akhilesh"
    }

        
