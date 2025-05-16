"""
# FastAPI
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.12+ based on standard Python type hints.
"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"status":True ,"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, item: str = None): 
    print(item_id)
    return {"item_id": item_id, "item": item}