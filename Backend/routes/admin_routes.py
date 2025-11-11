from fastapi import APIRouter

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/dashboard")
def admin_dashboard():
    return {"status": "Admin active"}
