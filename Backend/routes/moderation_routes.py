from fastapi import APIRouter

router = APIRouter(prefix="/moderation", tags=["Moderation"])

@router.get("/check")
def check_content():
    return {"status": "Clean ✅"}
