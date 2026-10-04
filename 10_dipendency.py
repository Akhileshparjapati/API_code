from fastapi import FastAPI, HTTPException, Header, Request,exceptions,Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app=FastAPI()

def common_func():
    return "This is 1st common function"

@app.get("/user")
def func_detail(data=Depends(common_func)):
    return{
        "data":data
    }

@app.post("/user")
def func_detail(data1=Depends(common_func)):
    return{
        "data":data1
    }

def verify_tocken(token:str = Header(None)):
    if token != "secretkey":
        raise HTTPException(
            status_code=401,
            detail="unauthorized access"
        )
    return{
        "user":"authorized user"
    }

@app.get("/secure")
def secure_data(user=Depends(verify_tocken)):
    return{
        "data":"this is secure data",
        "user":user
    }
