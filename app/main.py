from fastapi import FastAPI
from app.api.repo_routes import router as repo_router

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

app.include_router(repo_router, prefix="/repo")