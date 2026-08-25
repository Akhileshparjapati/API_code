from fastapi import FastAPI

app=FastAPI()

@app.get("/users")

def get_users(user_id:int):
    return {"users":user_id}

@app.get("/user")
def user_name(name: str =None):
    return {"name": name}

@app.get("/abc")

def get_abc(id:int = 10):
    return {"id": id}


@app.get("/item")
def get_list(name=None, id=5):
    return{
        "name":name,
        "id":10
    }