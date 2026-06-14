from fastapi import APIRouter, HTTPException, status

from api.models.todo import Todo  # جعلنا اسم todo صغير هنا ليتطابق مع اسم الملف
from api.schema.todo import GetTodo, PostTodo, PutTodo

todo_router = APIRouter(prefix="/api", tags=["TO DO"])


@todo_router.get("/")
async def all_todo():
    data = Todo.all()
    return await GetTodo.from_queryset(data)


@todo_router.post("/")
async def post_todo(body: PostTodo):
    row = await Todo.create(**body.dict(exclude_unset=True))
    return await GetTodo.from_tortoise_orm(row)


@todo_router.put("/")
async def update_todo(key: int, body: PutTodo):
    data = body.dict(exclude_unset=True)
    exists = await Todo.filter(id=key).exists()
    if not exists:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TODO NOT FOUND")
    
    await Todo.filter(id=key).update(**data)
    return await GetTodo.from_queryset_single(Todo.get(id=key))


@todo_router.delete("/{key}")
async def delete_todo(key: int):
    exists = await Todo.filter(id=key).exists()
    if not exists:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TODO NOT FOUND")
    
    await Todo.filter(id=key).delete()
    return "Todo deleted successfully."