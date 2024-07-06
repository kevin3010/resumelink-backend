from typing import List, Optional
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorCollection
from schemas.users import UserCreate, UserUpdate, UserResponse
from schemas.jobs import JobsCreate, JobsResponse
from core.database import jobs_collection

class CRUDJobs:
    def __init__(self, collection: AsyncIOMotorCollection):
        self.collection = collection

    async def insert_many(self, jobs_list: List[JobsCreate]) -> Optional[List[JobsResponse]]:
        
        jobs_list = [job.model_dump(by_alias=True) for job in jobs_list]
        result = await self.collection.insert_many(jobs_list)
        return result.inserted_ids


crud_job = CRUDJobs(jobs_collection)
