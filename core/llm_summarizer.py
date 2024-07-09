import json
import boto3
from .config import settings
from anthropic import Anthropic
from schemas.jobs import JobSummary

class Summarizer:
    def __init__(self):
        
        self.models = {
            "Sonnet": "claude-3-5-sonnet-20240620",
            "Haiku": "claude-3-haiku-20240307",
        }
        
        self.model_id = self.models[settings.ANTHROPIC_MODEL]
        
        self.job_summerizer_tool = ""
        with open("schemas/jobs.json", "r") as f:
            self.job_summerizer_tool= json.load(f)
            
        self.tools = [self.job_summerizer_tool]
        self.client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)
        

    def summarize(self,job_description):
        
        messages = [{
            "role": "user",
            "content":  job_description
        }] 
        
        response = self.client.messages.create(
            model=self.model_id,
            max_tokens=1000,
            tools=self.tools,
            messages=messages,
            tool_choice={"type": "tool", "name": "job_description_summerizer"}
        )
        
        summrization = JobSummary(jobs_summary=job_description, experience="")
        
        for content in response.content:
            if content.type == "tool_use" and content.name == "job_description_summerizer":
                summrization = JobSummary(**content.input)
                break
        
        return summrization
                
summarizer = Summarizer()