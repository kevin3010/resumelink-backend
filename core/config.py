from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    DATABASE_NAME: str
    FIREBASE_CREDENTIALS_PATH: str
    FIREBASE_CLIENT_CONFIG_PATH: str
    AWS_ACCESS_KEY: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_REGION: str
    
    S3_BUCKET_NAME: str = 'resume-link-bucket'
    S3_UPLOAD_PATH: str = 'resumes/'
    
    class Config:
        env_file = ".env"

settings = Settings()
