from fastapi import APIRouter

router = APIRouter(prefix="/community", tags=["Community"])

@router.get("/rooms")
def get_rooms():
    return {"rooms": ["AI Lounge", "Tech Hub"]}
