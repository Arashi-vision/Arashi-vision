python
from fastapi import APIRouter

admin_router = APIRouter()

@admin_router.get("/dashboard")
def dashboard():
    return {"admin": True}

