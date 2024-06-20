from typing import List
from fastapi import APIRouter, HTTPException, status
from crud.user import crud_user
from schemas.user import UserCreate, UserUpdate, UserResponse

router = APIRouter()

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user_in: UserCreate):
    return await crud_user.create(user_in)

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: str):
    user = await crud_user.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: str, user_in: UserUpdate):
    user = await crud_user.update(user_id, user_in)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}", response_model=UserResponse)
async def delete_user(user_id: str):
    user = await crud_user.remove(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
