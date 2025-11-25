
from fastapi import APIRouter

analytics_router = APIRouter()

@analytics_router.get("/stats")
def stats():
    return {"stats": []}

