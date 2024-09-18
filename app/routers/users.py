from fastapi import APIRouter, HTTPException, Request, Depends
from typing import List
from app.models import User

user_router = APIRouter()

# Dependency to get the MongoDB client from the app state
async def get_db(request: Request):
    if not hasattr(request.app, "mongodb"):
        raise HTTPException(status_code=500, detail="Database not connected")
    return request.app.mongodb

# Create user
@user_router.post("/api/v1/users", response_model=User)
async def insert_user(user: User, db = Depends(get_db)):
    existing_user = await db["users"].find_one({
        "$or": [
            {"email": user.email},
            {"phone": user.phone}
        ]
    })
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this email or phone number already exists")

    result = await db["users"].insert_one(user.dict())
    inserted_user = await db["users"].find_one({"_id": result.inserted_id})
    if inserted_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return inserted_user

# Read all users
@user_router.get("/api/v1/users")
# @user_router.get("/api/v1/users", response_model=List[User])
async def read_users(db = Depends(get_db)):
    users = await db["users"].find().to_list(None)
    for user in users:
        user["_id"] = str(user["_id"])  # Convert ObjectId to string
    return users

