from core.embeddings import embedding_store
from core.vector_store import vector_store
from core.config import settings
import csv
from jobspy import scrape_jobs
from schemas.jobs import JobsCreate
from crud.jobs import crud_job
from typing import List
from core.llm_summarizer import summarizer

async def fetch_jobs():

    jobs = scrape_jobs(
        site_name=["indeed"],
        search_term="software engineer",
        location="Canada",
        results_wanted=1,
        hours_old=72, # (only Linkedin/Indeed is hour specific, others round up to days old)
        country_indeed='Canada',  # only needed for indeed / glassdoor
        linkedin_fetch_description=True # get full description and direct job url for linkedin (slower)
    )

    jobs.rename(columns={"id": "job_id"}, inplace=True)
    jobs["timestamp"] = ""
    
    return [JobsCreate(**job) for job in jobs.to_dict(orient="records")]
    

async def generate_embeddings(jobs : List[JobsCreate]):
    
    job_descriptions = [summarizer.summarize(job.description).jobs_summary for job in jobs]
    jobs_embeddings = await embedding_store.generate_embeddings(job_descriptions)
    return jobs_embeddings
    
    
async def upsert_job_embeddings(jobs, jobs_embeddings, job_ids):
    jobs_vector = [ {"id" : str(job_id), "values": embedding.values, "metadata": {"job_id": str(job_id), "description": job.description}} for job, embedding, job_id in zip(jobs, jobs_embeddings, job_ids)]
    await vector_store.upsert_job_embeddings(jobs_vector)
    
async def start_processing_jobs(): 
    
    jobs = await fetch_jobs()
    jobs_embeddings = await generate_embeddings(jobs)
    job_id = await crud_job.insert_many(jobs)
    await upsert_job_embeddings(jobs, jobs_embeddings, job_id)
    
    
    
    
    