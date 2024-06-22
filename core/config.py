from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    DATABASE_NAME: str
    FIREBASE_CREDENTIALS_PATH: str

    class Config:
        env_file = ".env"

settings = Settings()
