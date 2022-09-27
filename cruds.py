from sqlalchemy.orm.session import Session
from fastapi import HTTPException
import db.models as m
import schemas as s

def create_todo_by_content(db: Session, content: str) -> s.Todo:
    todo_orm = m.Todo(
        content=content
    )
    db.add(todo_orm)
    db.commit()
    db.refresh(todo_orm)
    todo = s.Todo.from_orm(todo_orm)
    return todo

def get_all_todo(db:Session) -> list[s.Todo]:
    todos_orm = db.query(m.Todo).all()
    todos = list(map(s.Todo.from_orm, todos_orm))
    return todos

def delete_todo_by_id(db:Session, todo_id: int) -> None:
    todo = db.query(m.Todo).filter(m.Todo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="todo not found")
    db.delete(todo)
    db.commit()
    return     