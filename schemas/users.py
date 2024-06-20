from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId

class UserBase(BaseModel):
    name: str
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
        orm_mode = True
        json_encoders = {ObjectId: str}
