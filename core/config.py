from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    
    # Database Configurations
    DATABASE_URL: str
    DATABASE_NAME: str
    
    # Firebase Configurations
    FIREBASE_CREDENTIALS_PATH: str
    FIREBASE_CLIENT_CONFIG_PATH: str
    
    # AWS Configurations
    AWS_ACCESS_KEY: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_REGION: str
    
    #S3 Configurations
    S3_BUCKET_NAME: str = 'resume-link-bucket'
    S3_UPLOAD_PATH: str = 'resumes/'

    # Pinecone Configrations
    PINECONE_API_KEY: str
    PINECONE_INDEX_NAME_JOBS: str = "jobs"
    PINECONE_INDEX_NAME_RESUMES: str = "resumes"
    
    USERS_COLLECTION: str = "users"
    JOBS_COLLECTION: str = "jobs"
    
    class Config:
        env_file = ".env"

settings = Settings()
