# To install packages, run the following command:   uv add fastapi --extra standard
# To run the FastAPI application, use the command:   uv run fastapi dev
from fastapi import FastAPI

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"status": True, "message": "Hello World"}

user = [
    {""
    "id": 1,
    "name": "Mustafa",
    "age": 18
    },
    {
        "id": 2, 
        "name": "Abdullah",
        "age": 20
        }
]

@app.get("/user/{user_id}")
async def get_user(user_id: int):
    for i in user:
        if i["id"] == user_id:
            return {"status": True, "message": "User found", "data": i}
    return {"status": False, "message": "User not found"}
