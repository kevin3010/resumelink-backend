from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import json

ENV = "dev"

app = FastAPI()

class UploadResumeRequest(BaseModel):
    url: str
    userId: str

class KeywordsResponse(BaseModel):
    experience: List[str]
    technologies: List[str]
    skills: List[str]

class Job(BaseModel):
    CompanyName: str
    Date: str
    Location: str
    Position: str
    JobURL: str

class JobsListResponse(BaseModel):
    jobs: List[Job]


@app.post("/upload-resume")
async def upload_resume(request: UploadResumeRequest):
    # This is mock implementation, you can add logic to handle the files here
    data = request.dict()
    return {"message": "Resume data received", "data": data}

@app.get("/keywords", response_model=KeywordsResponse)
async def get_keywords():
    # Mock data, replace with actual logic
    keywords = KeywordsResponse(
        experience=["5 years at Company A", "2 years at Company B"],
        technologies=["Python", "FastAPI", "SQL"],
        skills=["Data Analysis", "Machine Learning"]
    )
    return keywords


@app.get("/list-of-jobs", response_model=JobsListResponse)
async def list_of_jobs():
    jobs = []
    with open("Jobs/jobs_test.jsonl", "r") as file:
        for line in file:
            job_data = json.loads(line)
            job = Job(
                CompanyName=job_data["company_name"],
                Date=job_data["date"],
                Location=job_data["location"],
                Position=job_data["position"],
                JobURL=job_data["job_url"]
            )
            jobs.append(job)
    response = JobsListResponse(jobs=jobs)
    return response


# To run the server, use the command: uvicorn main:app --reload
# Make sure this script is named main.py or change accordingly in the above command.