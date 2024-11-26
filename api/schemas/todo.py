from pydantic import BaseModel, Field
from typing import Optional
from tortoise.contrib.pydantic import pydantic_queryset_creator
from api.models.todo import Todo

get_todo = pydantic_queryset_creator(Todo, name="Todo")


class PostTodo(BaseModel):
    task: str = Field(..., max_length=100)
    done: bool


class PutTodo(BaseModel):
    task: Optional[str] = Field(None, max_length=100)
    done: Optional[bool]