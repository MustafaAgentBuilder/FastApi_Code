from fastapi import FastAPI , Path

app = FastAPI()


@app.get("/")
async def root():
    return {"Status":True ,"message": "Second API"}


items = [
    {"id": 1, "name": "Apple", "price": 100, "category": "Fruit", "in_stock": True},
    {"id": 2, "name": "Banana", "price": 40, "category": "Fruit", "in_stock": True},
    {"id": 3, "name": "Mango", "price": 150, "category": "Fruit", "in_stock": False},
    {"id": 4, "name": "Carrot", "price": 30, "category": "Vegetable", "in_stock": True},
    {"id": 5, "name": "Milk", "price": 120, "category": "Dairy", "in_stock": True}
]

# Static method to get all items
@app.get("/items")
async def read_items():
    return items

# Dynamic method to get item by id
@app.get("/item/{id}", summary="🔎 Search Item by ID", description="📝 Enter the item ID number to search from the list.")
async def give_data(
    id: int = Path(..., title="Item ID", description="Enter ID number (e.g., 1, 2, 3...)", ge=1)
):
    for i in items:
        if i['id'] == id:
            return {"status": True, "message": "✅ Item Found", "data": i}
    return {"status": False, "message": "❌ Item Not Found", "data": None}