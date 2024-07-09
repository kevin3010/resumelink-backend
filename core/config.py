from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    
    # Database Configurations
    DATABASE_URL: str
    DATABASE_NAME: str
    
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
    
    
    # FireBase Admin Config
    FIREBASE_ADMIN_TYPE: str
    FIREBASE_ADMIN_PROJECT_ID: str
    FIREBASE_ADMIN_PRIVATE_KEY_ID: str
    FIREBASE_ADMIN_PRIVATE_KEY: str
    FIREBASE_ADMIN_CLIENT_EMAIL: str
    FIREBASE_ADMIN_CLIENT_ID: str
    FIREBASE_ADMIN_AUTH_URI: str
    FIREBASE_ADMIN_TOKEN_URI: str
    FIREBASE_ADMIN_AUTH_PROVIDER_X509_CERT_URL: str
    FIREBASE_ADMIN_CLIENT_X509_CERT_URL: str
    FIREBASE_ADMIN_UNIVERSE_DOMAIN: str


    # FireBase Client Config
    FIREBASE_CLIENT_APIKEY: str
    FIREBASE_CLIENT_AUTHDOMAIN: str
    FIREBASE_CLIENT_PROJECTID: str
    FIREBASE_CLIENT_STORAGEBUCKET: str
    FIREBASE_CLIENT_MESSAGINGSENDERID: str
    FIREBASE_CLIENT_APPID: str
    FIREBASE_CLIENT_MEASUREMENTID: str
    FIREBASE_CLIENT_DATABASEURL: str
    
    
    # Anthropic Config
    ANTHROPIC_API_KEY: str
    ANTHROPIC_MODEL: str

    class Config:
        env_file = ".env"

settings = Settings()
