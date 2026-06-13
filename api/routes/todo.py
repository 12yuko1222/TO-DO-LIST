from fastapi import APIRouter

todo_router=APIRouter(prefix = "/api", tags=["TO DO"])


@todo_router.get("/")
def all_todo():
    return "Not implemented"


@todo_router.post("/")
def post_todo():
    return "Not Impelemented"

@todo_router.put("/")
def update_todo(key:int):
    return "Not Implemented"

@todo_router.delete("/{key}")
def delete_todo(key:int):
    return "Not Implemented"














