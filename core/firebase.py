import firebase_admin
from firebase_admin import credentials,auth
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends,HTTPException
from .config import settings
import pyrebase
import json 

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

def initialize_firebase_client():
    
    with open(settings.FIREBASE_CLIENT_CONFIG_PATH, "r") as f:
        config = json.load(f)
    
    firebase = pyrebase.initialize_app(config)
    return firebase

if not firebase_admin._apps:
    initialize_firebase()
    

firebase_client = initialize_firebase_client()
    
