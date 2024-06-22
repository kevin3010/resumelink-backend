from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId

class UserBase(BaseModel):
    user_id: str
    name: str
    email: str
    resume: str
    keywords: List[str]

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

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
