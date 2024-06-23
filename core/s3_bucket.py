import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
from .config import settings

session = boto3.Session(
    aws_access_key_id=settings.AWS_ACCESS_KEY,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name=settings.AWS_REGION
)

s3 = session.resource('s3')