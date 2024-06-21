from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "***REMOVED***"
    DATABASE_NAME: str = "resume_link_db"

    class Config:
        env_file = ".env"

settings = Settings()
