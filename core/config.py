from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "fastapi_db"

    class Config:
        env_file = ".env"

settings = Settings()
