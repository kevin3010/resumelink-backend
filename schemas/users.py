from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId
from typing import Optional


class UserBase(BaseModel):
    user_id: str
    name: str
    email: str
    resume_path: Optional[str] = None
    resume_text: Optional[str] = None
    jobs: Optional[List[str]] = None
    resume_embeddings: Optional[List[float]] = None
    keywords: Optional[List[str]] = None

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    user_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    resume: Optional[str] = None
    keywords: Optional[List[str]] = None

class UserInDB(UserBase):
    id: str = Field(default_factory=lambda: str(ObjectId()))

class UserResponse(UserInDB):
    class Config:
        from_attributes = True
        json_encoders = {ObjectId: str}
        
class UserLoginResponse(BaseModel):
    user_id : str
    token : str
        

class SignUpSchema(BaseModel):
    email:str
    password:str

    class Config:
        json_schema_extra ={
            "example":{
                "email":"sample@gmail.com",
                "password":"samplepass123"
            }
        }


class LoginSchema(BaseModel):
    email:str
    password:str

    class Config:
        schema_extra ={
            "example":{
                "email":"sample@gmail.com",
                "password":"samplepass123"
            }
        }
