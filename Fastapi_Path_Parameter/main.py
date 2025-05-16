# 1. Path Parameters     → Used to get values directly from the URL path.

# 2. Path Parameters → BEST for identifying a specific resource
#    Example: /user/123  →  Get user with ID 123
#    Use for: IDs, usernames, slugs


from fastapi import FastAPI

app = FastAPI()

# Path parameter: user_id will come from the URL
@app.get("/user/{user_id}")
async def get_user(user_id: int):
    return {"message": f"User ID received: {user_id}"}
