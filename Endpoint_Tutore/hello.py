# This file defines FastAPI endpoints for user queries related to roll numbers.
from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from typing import Optional
from uuid import uuid4
from main import 
app = FastAPI()



@app.get("/user")
async def greet():
    return {"message": "Welcome to Ai Tutore"}
# Mock user database: user_id -> user data


db_users = {
    "R001": {"user_id": "R001", "name": "Mustafa"},
    "R002": {"user_id": "R002", "name": "Uzair"},
    "R003": {"user_id": "R003", "name": "Khurram"},
}

class MessageRequest(BaseModel):
    message: str
    user_id: Optional[str] = None
    name: Optional[str] = None

@app.post("/user/query")
async def user_query(req: MessageRequest):
    """
    1) Require `message` plus at least one of: user_id OR name.
    2) If both are provided, use `user_id`.
    3) Verify the user exists in `db_users`.
    4) Return dummy response if OK, otherwise 400/404 error.
    """
    # 1) At least one identifier must be provided
    if not req.user_id and not req.name:
        raise HTTPException(
            status_code=400,
            detail="Please provide at least one of: user_id OR name."
        )

    # 2) Choose identifier: user_id if present, otherwise name
    if req.user_id:
        key, value = "user_id", req.user_id
        user = db_users.get(value)
    else:
        key, value = "name", req.name
        user = next(
            (u for u in db_users.values() if u["name"].lower() == value.lower()),
            None
        )

    # 3) If not found in DB, raise 404
    if user is None:
        raise HTTPException(
            status_code=404,
            detail=f"No user found with {key} = '{value}'."
        )

    # 4) Dummy agent response
    return {
        "status": "success",
        "user": user,
        "your_message": req.message,
        "agent_response": f"Hello {user['name']}! We received your message: '{req.message}'."
    }




# @app.post("/user/signin")
# async def user_signin(query: UserQuery):
#     if not query.name:
#         raise HTTPException(status_code=400, detail="Name is required for sign in.")
#     roll_no = USER_DB.get(query.name)
#     if roll_no:
#         return {"message": "Welcome back!", "name": query.name, "roll_no": roll_no}
#     # Generate a new roll number (simple UUID-based, or incrementing logic)
#     new_roll_no = f"R{str(len(USER_DB)+1).zfill(3)}"
#     USER_DB[query.name] = new_roll_no
#     return {"message": "User registered successfully.", "name": query.name, "roll_no": new_roll_no}



# @app.post("/user/login")
# async def user_login(query: UserQuery):
#     if not query.roll_no:
#         raise HTTPException(status_code=400, detail="Roll number is required for login.")
#     for name, rn in USER_DB.items():
#         if rn == query.roll_no:
#             return {"message": "Login successful.", "name": name, "roll_no": rn}
#     raise HTTPException(status_code=404, detail="Roll number not found. Please sign in first.")





# @app.post("/assistant/message")
# async def assistant_message(request: MessageRequest):
#     """
#     Accepts a message and user_id, fetches the user, and forwards the message to an agent/service.
#     """
#     # 1. Fetch user from mock DB
#     user = db_users.get(request.user_id)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found.")
#     # 2. Forward message and user data to agent/service
#     agent_response = await forward_message_to_agent(request.message, user)
#     # 3. Return the agent's response
#     return agent_response