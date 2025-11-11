from fastapi import APIRouter

router = APIRouter(prefix="/voice", tags=["Voice"])

@router.get("/test")
def voice_test():
    return {"message": "Voice module active"}
