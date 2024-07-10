from crud.user import crud_user
from schemas.users import UserUpdate, UserBase, UserResponse
from typing import List
from core.vector_store import vector_store
from crud.jobs import crud_job


async def find_matching_jobs(user: UserUpdate):
    jobs = await vector_store.query_jobs(user.resume_embeddings, metadata=False, top_k=10)
    jobs = [job["id"] for job in jobs['matches']]
    return jobs    
    

async def process_user(users: List[UserResponse]):
    for user in users:
        user.jobs = await find_matching_jobs(user)
        results = await crud_user.update(user.user_id, UserUpdate(user_id=user.user_id, jobs=user.jobs))


async def start_processing_users(): 
    users = await crud_user.get_users()
    await process_user(users)