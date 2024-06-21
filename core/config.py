from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "mongodb+srv://admin:kevinandjevin@resumelink.ctj0men.mongodb.net/?retryWrites=true&w=majority&appName=ResumeLink"
    DATABASE_NAME: str = "resume_link_db"

    class Config:
        env_file = ".env"

settings = Settings()
