from pydantic import BaseModel

class TodoPayload(BaseModel):
    content: str

class Todo(BaseModel):
    id: int
    content: str

    class Config:
        orm_mode = True