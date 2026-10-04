from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
todos=[]

class Todo(BaseModel):
    id:int
    title: str
    completed: bool

@app.post("/todos")

def todos_list(todo:Todo):
    todos.append(todo)
    return {"message":"todos added","data":todo}


@app.get("/todos")

def get_todo():
    return todos

@app.get("/todos/{todo_id}")

def todo_list(todo_id:int):
    for todo in todos:
        if todo.id==todo_id:
            return todo
    return {"error":"todo not found"}


@app.put("/todos/{todo_id}")
def update_todo(todo_id:int,updated_todo:Todo):
    for index,todo in enumerate(todos):
        if todo.id==todo_id:
            todos[index]=updated_todo
            return{
                "data":"updated todo",
                "data":updated_todo
            }
    return {"error":"not updated"}



@app.delete("/todos/{todo_id}")
def delete_data(todo_id:int):
    for index, todo in enumerate(todos):
        if todo.id==todo_id:
            todos.pop(index)
            return {"data":"delete success"}
    return {"error":"not delete"}
    