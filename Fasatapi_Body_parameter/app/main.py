# In FastAPI, there are three main types of parameters used to receive data from the user:
# 1. Path Parameters     → Used to get values directly from the URL path.
# 2. Query Parameters    → Used to get values from the URL query string (after '?').
# 3. Body Parameters     → Used to get data from the request body (usually in POST, PUT methods).
# These parameters help collect input from the client in different ways depending on the use case.

from fastapi import FastAPI 
from pydantic import BaseModel , Field , EmailStr 


app = FastAPI()

class User(BaseModel):
    name: str = Field(..., title="Name of the user", max_length=50)
    email: EmailStr = Field(..., title="Email of the user")
    age: int = Field(..., gt=0, le=120, title="Age of the user")
    is_active: bool = Field(default=True, title="Is the user active?")
    bio: str | None = Field(default=None, title="Bio of the user", max_length=200)

@app.get("/" , status_code=status.HTTP_200_OK)
async def read_root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": "Welcome to the FastAPI application!"}

@app.post("/user/")
async def create_user(user: User):
    """
    Create a new user with the provided details.
    """
    print(f"Type of user before: {type(user)}")
    user_dict = user.model_dump()  # for Pydantic v2
    print(f"Type of user after: {type(user_dict)}")

    user_data = {
        "name": user.name,
        "email": user.email,
        "age": user.age,
        "is_active": user.is_active,
        "bio": user.bio
    }

    return {"message": "User created successfully!", "user": user_data}



# 1. Path Parameters → BEST for identifying a specific resource
#    Example: /user/123  →  Get user with ID 123
#    Use for: IDs, usernames, slugs

# 2. Query Parameters → BEST for filters, search, optional values
#    Example: /search?name=Ali&age=25
#    Use for: Search, filter, sort, pagination

# 3. Body Parameters → BEST for sending large or complex data (like JSON)
#    Example: POST /user with JSON body
#    {
#      "name": "Ali",
#      "email": "ali@example.com"
#    }
#    Use for: Creating or updating data (POST, PUT), forms, authentication
