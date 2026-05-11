from fastapi import APIRouter
from app.services.repo_loader import get_code_files

router = APIRouter()

@router.get("/health")
def repo_health():
    return {"repo" : "ok"}

@router.get("/scan")
def scan_repo():
    files = get_code_files(".")
    return {"files": files}

