from fastapi import FastAPI
from api.endpoints import users
from contextlib import asynccontextmanager
from core.firebase import initialize_firebase
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    docs_url="/api/docs",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_firebase()
    yield

app.include_router(users.router, prefix="/api/users", tags=["users"])

@app.get("/health")
async def health_check():
    return {"status": "OK"}

@app.get("/")
async def home():
    return {"status": "OK"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
