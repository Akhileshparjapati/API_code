from fastapi import FastAPI, HTTPException, Request,exceptions
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app=FastAPI()

class UserNotFoundException(Exception):
    def __init__(self,name):
        self.name=name

@app.exception_handler(UserNotFoundException)
def global_exception_hand(request:Request,exc:UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"message":f"User {exc.name} not found"}
    )

@app.get("/user/{name}")
def user_got(name:str):
    if name !="Akhil":
        raise UserNotFoundException(name=name)
    return{
        "Name":name
    }



# @app.get("/user/{user_id}")
# def get_det(user_id:int):
#     if user_id !=1:
#         raise HTTPException(
#             status_code=404,
#             detail="user not available"
#         )
#     return{
#         "id":1,
#         "name":"Akhilesh"

#     }