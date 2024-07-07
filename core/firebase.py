import firebase_admin
from firebase_admin import credentials,auth
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends,HTTPException
from .config import settings
import pyrebase
import json 
import base64

security = HTTPBearer()

firebase_admin_config = {
    "type" : settings.FIREBASE_ADMIN_TYPE,  
    "project_id": settings.FIREBASE_ADMIN_PROJECT_ID,
    "private_key_id": settings.FIREBASE_ADMIN_PRIVATE_KEY_ID,
    "private_key": base64.b64decode(settings.FIREBASE_ADMIN_PRIVATE_KEY).decode('utf-8'),
    "client_email": settings.FIREBASE_ADMIN_CLIENT_EMAIL,
    "client_id": settings.FIREBASE_ADMIN_CLIENT_ID,
    "auth_uri": settings.FIREBASE_ADMIN_AUTH_URI,
    "token_uri": settings.FIREBASE_ADMIN_TOKEN_URI,
    "auth_provider_x509_cert_url": settings.FIREBASE_ADMIN_AUTH_PROVIDER_X509_CERT_URL,
    "client_x509_cert_url": settings.FIREBASE_ADMIN_CLIENT_X509_CERT_URL,
    "universe_domain": settings.FIREBASE_ADMIN_UNIVERSE_DOMAIN
}

firebase_client_config = {
    "apiKey": settings.FIREBASE_CLIENT_APIKEY,
    "authDomain": settings.FIREBASE_CLIENT_AUTHDOMAIN,
    "projectId":settings.FIREBASE_CLIENT_PROJECTID,
    "storageBucket": settings.FIREBASE_CLIENT_STORAGEBUCKET,
    "messagingSenderId": settings.FIREBASE_CLIENT_MESSAGINGSENDERID,
    "appId":settings.FIREBASE_CLIENT_APPID,
    "measurementId":settings.FIREBASE_CLIENT_MEASUREMENTID,
    "databaseURL":settings.FIREBASE_CLIENT_DATABASEURL
}

def initialize_firebase():
    cred = credentials.Certificate(firebase_admin_config)
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
    
    firebase = pyrebase.initialize_app(firebase_client_config)
    return firebase

if not firebase_admin._apps:
    initialize_firebase()
    

firebase_client = initialize_firebase_client()
    
