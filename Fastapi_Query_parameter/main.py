# 1. Query Parameters    → Used to get values from the URL query string (after '?').


# 2. Query Parameters → BEST for filters, search, optional values
#    Example: /search?name=Ali&age=25
#    Use for: Search, filter, sort, pagination

from fastapi import FastAPI

app = FastAPI()

# Query parameters: name and age come after ?
@app.get("/search/")
async def search_user(name: str, age: int):
    return {"message": f"Search for user: {name}, Age: {age}"}
