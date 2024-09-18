from fastapi import FastAPI, HTTPException
from app.db import lifespan
from app.routers.users import user_router

app = FastAPI(lifespan=lifespan)
# Include the routes from the router
app.include_router(user_router)

@app.get("/")
def root():
    return {"message": "Hello there ✋"}
