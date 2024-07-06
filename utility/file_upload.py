from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
from core.s3_bucket import s3
from core.config import settings

async def upload_file(file_obj,file_name):
    try:
        await s3.Bucket(settings.S3_BUCKET_NAME).upload_fileobj(file_obj, settings.S3_UPLOAD_PATH+file_name)
    except ClientError as e:
        print(f"Failed to upload file: {e}")
    except Exception as e:
        print(str(e))
        