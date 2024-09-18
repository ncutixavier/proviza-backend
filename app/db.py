
from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.config import MONGO_URL, DB_NAME

# define a lifespan method for fastapi
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Start the database connection
    await startup_db_client(app)
    yield
    # Close the database connection
    await shutdown_db_client(app)

# method for start the MongoDb Connection
async def startup_db_client(app):
    app.mongodb_client = AsyncIOMotorClient(MONGO_URL)
    app.mongodb = app.mongodb_client.get_database(DB_NAME)
    print("--> DB CONNECTED <--")

# method to close the database connection
async def shutdown_db_client(app):
    app.mongodb_client.close()
    print("--> DB DISCONNECTED <--")