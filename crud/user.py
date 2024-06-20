from typing import List, Optional
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorCollection
from schemas.users import UserCreate, UserUpdate, UserResponse
from core.database import users_collection

class CRUDUser:
    def __init__(self, collection: AsyncIOMotorCollection):
        self.collection = collection

    async def create(self, user_in: UserCreate) -> UserResponse:
        user = user_in.dict()
        result = await self.collection.insert_one(user)
        user["id"] = str(result.inserted_id)
        return UserResponse(**user)

    async def get(self, id: str) -> Optional[UserResponse]:
        user = await self.collection.find_one({"_id": ObjectId(id)})
        if user:
            user["id"] = str(user["_id"])
            return UserResponse(**user)

    async def update(self, id: str, user_in: UserUpdate) -> Optional[UserResponse]:
        user = {k: v for k, v in user_in.dict().items() if v is not None}
        result = await self.collection.update_one({"_id": ObjectId(id)}, {"$set": user})
        if result.modified_count == 1:
            user = await self.get(id)
            return user

    async def remove(self, id: str) -> Optional[UserResponse]:
        user = await self.collection.find_one({"_id": ObjectId(id)})
        if user:
            await self.collection.delete_one({"_id": ObjectId(id)})
            user["id"] = str(user["_id"])
            return UserResponse(**user)

crud_user = CRUDUser(users_collection)
