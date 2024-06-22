from typing import List
from fastapi import APIRouter, HTTPException, status, File, UploadFile
from fastapi.responses import JSONResponse
from crud.user import crud_user
from schemas.users import UserCreate, UserUpdate, UserResponse, SignUpSchema, LoginSchema, UserLoginResponse
from fastapi import APIRouter, Depends
from firebase_admin import auth
from core.firebase import verify_token, firebase_client

import os

router = APIRouter()

@router.post("/signup",response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def signup(user: SignUpSchema):
    try:
        f_user = auth.create_user(email=user.email, password=user.password)
        user_id = f_user._data["localId"]
        d_user = await crud_user.create(UserCreate(user_id=user_id, email=user.email , name="", resume="", keywords=[]))
        return d_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", response_model=UserLoginResponse, status_code=status.HTTP_200_OK)
async def login(user: LoginSchema):
    try:
        user = firebase_client.auth().sign_in_with_email_and_password(user.email, user.password)
        return UserLoginResponse(user_id=user["localId"], token=user["idToken"])
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/protected-route")
async def protected_route(decoded_token: dict = Depends(verify_token)):
    return {"msg": "This is a protected route", "user_id": decoded_token["uid"]}

# @router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
# async def create_user(user_in: UserCreate):
#     return await crud_user.create(user_in)

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

