from motor.motor_asyncio import AsyncIOMotorClient
from .config import settings

client = AsyncIOMotorClient(settings.DATABASE_URL)
database = client[settings.DATABASE_NAME]
users_collection = database.get_collection("users")
jobs_collection = database.get_collection("jobs")
