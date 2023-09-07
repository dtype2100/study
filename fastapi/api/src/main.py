from typing import List
from fastapi import Depends, FastAPI, Body, HTTPException
from pydantic import BaseModel
from database.connection import get_db
from sqlalchemy.orm import Session
from database.orm import Todo
from repository import get_todos
from schema.response import ListToDoRespinse
from schema.response import ToDoSchema
from repository import *
from flask import session


app = FastAPI()

@app.get("/")
def health_check_handler():
    return {"status": "ok"}

todo_data = {
    1: {
        "id": 1,
        "contents": "실전! FastAPI 섹션 0 수강",
        "is_done": True,
    },
    2: {
        "id": 2,
        "contents": "실전! FastAPI 섹션 1 수강",
        "is_done": False,
    },
    3: {
        "id": 3,
        "contents": "실전! FastAPI 섹션 3 수강",
        "is_done": False,
    },
}


@app.get("/todos", status_code=200)
def get_todos_handler(order: str | None = None,
                      session: Session = Depends(get_db),
                      ): # 쿼리 파라미터
    todos: List[Todo]= get_todos(session=session)
    # ret = list(todo_data.values())
    if order == "DESC":
        return ListToDoRespinse(
            todos=[ToDoSchema.from_orm(todo) for todo in todos[::-1]]
        ) # todos[::-1] # ret[::-1]
    return ListToDoRespinse(
        todos=[ToDoSchema.from_orm(todo) for todo in todos]
    ) # todos # ret

@app.get("/todos/{todo_id}", status_code=200)
def get_todo_handler(todo_id: int,
                     session: Session = Depends(get_db),
                     ) -> ToDoSchema:
    # todo = todo_data.get(todo_id)
    todo: Todo | None = get_todo_by_todo_id(session=session, todo_id=todo_id) #
    if todo:
        return ToDoSchema.from_orm(todo)
    return HTTPException(status_code=404, detail="Todo Not Found")

class CreateTodoRequest(BaseModel):
    id: int
    contents: str
    is_done: bool

@app.post("/todos", status_code=201)
def create_todo_handler(request: CreateTodoRequest):
    todo_data[request.id] = request.dict()
    return todo_data[request.id]

@app.patch("/todos/{todo_id}", status_code=200)
def update_todo_handler(todo_id: int, 
                        is_done: bool = Body(..., embed=True)): # 하나의 컬럼값?
    todo = todo_data.get(todo_id)
    if todo:
        todo["is_done"] = is_done
        return todo
    return HTTPException(status_code=404, detail="Todo Not Found")

@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo_handler(todo_id: int):
    todo = todo_data.pop(todo_id, None)
    if todo:
        return todo
    return HTTPException(status_code=404, detail="Todo Not Found")
