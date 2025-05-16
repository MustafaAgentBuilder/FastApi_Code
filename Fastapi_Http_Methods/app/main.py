from fastapi import FastAPI, HTTPException
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI()

# 🧠 Fake database
fake_users_db = []

# ✅ User model
class UserInfo(BaseModel):
    name: str
    age: int
    height: Optional[float] = None
    location: Optional[str] = None
    hobbies: Optional[List[str]] = None
    email: Optional[str] = None
    phone: Optional[str] = None

# ✅ Add multiple users
@app.post("/user/many/")
async def create_many_users(users: List[UserInfo]):
    fake_users_db.extend(users)
    return {"message": "Users added successfully", "total_users": len(fake_users_db)}

# ✅ Get user by ID (index)
@app.get("/user/{user_id}")
async def get_user(user_id: int):
    try:
        return {"user_id": user_id, "user": fake_users_db[user_id]}
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")

# ✅ Update user by ID
@app.put("/user/{user_id}")
async def update_user(user_id: int, user: UserInfo):
    try:
        fake_users_db[user_id] = user
        return {"message": "User updated", "user": user}
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")

# ✅ Delete user by ID
@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    try:
        deleted_user = fake_users_db.pop(user_id)
        return {"message": "User deleted", "deleted_user": deleted_user}
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")

# ✅ Patch (partial update) user
@app.patch("/user/{user_id}")
async def patch_user(user_id: int, user: UserInfo):
    try:
        stored_user = fake_users_db[user_id]
        updated_user = user.dict(exclude_unset=True)

        # update only given fields
        for key, value in updated_user.items():
            setattr(stored_user, key, value)

        fake_users_db[user_id] = stored_user
        return {"message": "User patched", "user": stored_user}
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")
