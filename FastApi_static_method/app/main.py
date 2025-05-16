from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"status": True, "message": "Hello World"}

# This is your static user data
user = [
    {
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

# Static method - manual response for each ID
@app.get("/user/1")
async def get_user_1():
    return {"status": True, "message": "Static user 1", "data": user[0]}

@app.get("/user/2")
async def get_user_2():
    return {"status": True, "message": "Static user 2", "data": user[1]}
