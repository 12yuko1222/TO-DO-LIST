from pydantic import BaseModel, Field  # تم تصحيح الاملاء هنا
from typing import Optional
from tortoise.contrib.pydantic import pydantic_model_creator
from api.models.todo import Todo # انتبه لحالة الاحرف في اسم المجلد والملف Todo

GetTodo = pydantic_model_creator(Todo, name="To Do")

class PostTodo(BaseModel):
    task: str = Field(..., max_length=100)
    done: bool  # تم تصحيح علامة = إلى : هنا


class PutTodo(BaseModel):
    task: Optional[str] = Field(None, max_length=100)
    done: Optional[bool]