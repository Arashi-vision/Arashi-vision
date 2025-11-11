from fastapi import APIRouter

router = APIRouter(prefix="/analytics", tags=["Analytics"])

@router.get("/overview")
def analytics_data():
    return {"visits": 150, "users": 42}
