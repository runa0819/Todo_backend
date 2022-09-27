from fastapi import FastAPI, Depends
from sqlalchemy.orm.session import Session
from db.database import engine, get_db
from db.models import Base
import cruds as cr
import schemas as s

Base.metadata.create_all(bind=engine)


app = FastAPI()

@app.get("/hello")
async def hello():
    return {"message" : "Hello "}

@app.post("/todo", response_model=s.Todo)
async def create_todo(payload: s.TodoPayload, db: Session = Depends(get_db)):
    todo = cr.create_todo_by_content(db, payload.content)
    return todo

@app.get("/todos", response_model=list[s.Todo])
async def get_todos(db: Session = Depends(get_db)):
    todos = cr.get_all_todo(db)
    return todos

@app.delete("/todo/{id}")
async def delete_todo(id: int, db: Session = Depends(get_db)):
    cr.delete_todo_by_id(db, id)
    return {"detail" : "OK!!"}
