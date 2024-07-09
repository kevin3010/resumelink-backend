from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId
from typing import Optional

class JobsBase(BaseModel):
    job_id: str
    job_url: str
    job_url_direct: str
    title: str
    company: str
    location: str
    description: str
    timestamp: str
    

class JobsCreate(JobsBase):
    pass


class JobSummary(BaseModel):
    jobs_summary: str
    experience: str
    
class JobsResponse(JobsBase):
    class Config:
        from_attributes = True
        json_encoders = {ObjectId: str}

