import firebase_admin
from firebase_admin import credentials,auth
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends,HTTPException
from .config import settings

security = HTTPBearer()



def initialize_firebase():
    cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS_PATH)
    firebase_admin.initialize_app(cred)

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        print(credentials)
        decoded_token = auth.verify_id_token(credentials.credentials)
        print("Kevin")
        print(decoded_token)
        return decoded_token
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

if not firebase_admin._apps:
    initialize_firebase()
    
    
