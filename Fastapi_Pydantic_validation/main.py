from fastapi import FastAPI ,HTTPException
from pydantic import BaseModel
from typing import Optional



app = FastAPI()
class UserLocation(BaseModel):
    country: str
    city: str

class User(BaseModel):
    id: int
    name: str 
    age: int
    location: list[UserLocation]
    email: Optional[str] 


users_db = {}

# POST: Save a user
@app.post("/users/")
async def create_user(user_id: int, user: User):
    users_db[user_id] = user
    return {"message": "User created", "user_id": user_id, "user": user}

# GET: Get user by ID
@app.get("/users/{user_id}")
async def read_user(user_id: int):
    if user_id in users_db:
        return {"user_id": user_id, "user": users_db[user_id]}
    else:
        raise HTTPException(status_code=404, detail="User not found")