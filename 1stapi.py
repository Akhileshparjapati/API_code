from fastapi import FastAPI
app =FastAPI()




@app.get("/")
def home():
    return {"message":"hello"}


@app.get("/about")

def about():
    return {"message":"this is about page"}

@app.get("/user")

def user():
    return {"user":["akhil","vip","reema"]}



