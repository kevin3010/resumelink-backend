from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class UploadResumeRequest(BaseModel):
    url: str
    userId: str

class KeywordsResponse(BaseModel):
    experience: List[str]
    technologies: List[str]
    skills: List[str]

class Job(BaseModel):
    experience: str
    name: str
    role: str
    location: str
    salary: str
    portal: str
    link: str
    commonSkills: str
    otherSkills: str

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
    # Mock data, replace with actual logic
    jobs = [
        Job(
            experience="5+ years",
            name="Senior Developer",
            role="Backend Developer",
            location="Remote",
            salary="$120,000",
            portal="Indeed",
            link="https://example.com/job1",
            commonSkills="Python, FastAPI",
            otherSkills="Docker, Kubernetes"
        ),
        Job(
            experience="3+ years",
            name="Data Scientist",
            role="Data Scientist",
            location="New York, NY",
            salary="$110,000",
            portal="LinkedIn",
            link="https://example.com/job2",
            commonSkills="Python, SQL",
            otherSkills="TensorFlow, Keras"
        ),
    ]
    response = JobsListResponse(jobs=jobs)
    return response


# To run the server, use the command: uvicorn main:app --reload
# Make sure this script is named main.py or change accordingly in the above command.