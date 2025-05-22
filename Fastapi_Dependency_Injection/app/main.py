from fastapi import FastAPI, Depends
from typing import Annotated

app = FastAPI()

def user(name: str, age: int, country: str, city: str) -> dict:
    return {"user": name, "age": age, "country": country, "city": city}

@app.get("/")
async def read_root():
    return {"Status": True, "Hello": "User"}

# ✅ Correct usage of Annotated
@app.post("/user")
async def create_user(user: Annotated[dict, Depends(user)]):
    return user
