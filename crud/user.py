from typing import List, Optional
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorCollection
from schemas.users import UserCreate, UserUpdate, UserResponse
from core.database import users_collection

class CRUDUser:
    def __init__(self, collection: AsyncIOMotorCollection):
        self.collection = collection
        
    async def get_users(self) -> List[UserResponse]:
        users = []
        async for user in self.collection.find():
            user["id"] = str(user["_id"])
            users.append(UserResponse(**user))
        return users

    async def create(self, user_in: UserCreate) -> UserResponse:
        user = user_in.model_dump()
        result = await self.collection.insert_one(user)
        user["id"] = str(result.inserted_id)
        return UserResponse(**user)

    async def get(self, user_id: str) -> Optional[UserResponse]:
        user = await self.collection.find_one({"user_id": user_id})
        if user:
            user["id"] = str(user["_id"])
            return UserResponse(**user)

    async def update(self, user_id: str, user_in: UserUpdate) -> Optional[UserResponse]:
        user = {k: v for k, v in user_in.model_dump().items() if v is not None}
        result = await self.collection.update_one({"user_id": user_id}, {"$set": user})
        if result.matched_count == 1:
            user = await self.get(user_id)
            return user

    async def remove(self, user_id: str) -> Optional[UserResponse]:
        user = await self.collection.find_one({"user_id": user_id})
        if user:
            await self.collection.delete_one({"user_id": user_id})
            user["id"] = str(user["_id"])
            return UserResponse(**user)

crud_user = CRUDUser(users_collection)
