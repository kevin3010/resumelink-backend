from typing import List
from fastapi import APIRouter, HTTPException, status, File, UploadFile
from fastapi.responses import JSONResponse
from crud.user import crud_user
from schemas.users import UserCreate, UserUpdate, UserResponse, SignUpSchema, LoginSchema, UserLoginResponse
from fastapi import APIRouter, Depends
from firebase_admin import auth
from core.firebase import verify_token, firebase_client
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
from utility.file_upload import upload_file
from time import time
from utility.read_pdf import read_pdf

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
    user_in.user_id = user_id
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


@router.post("/{user_id}/upload-resume")
async def upload_file_endpoint(user_id: str, file: UploadFile = File(...)):
    try:
        
        filename = file.filename.split(".")[0].strip()
        filename = filename + "__" + user_id + "__" + str(int(time())) + ".pdf"
        upload_file(file.file, filename)
        
        content = await file.read()
        text = read_pdf(content)
        
        
        user_in = UserUpdate(user_id=user_id, resume=filename)
        user = await crud_user.update(user_id, user_in)
    
        return user
    except NoCredentialsError:
        raise HTTPException(status_code=401, detail="Credentials not available.")
    except PartialCredentialsError:
        raise HTTPException(status_code=401, detail="Incomplete credentials provided.")
    except ClientError as e:
        raise HTTPException(status_code=500, detail=f"Failed to upload file: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

