from fastapi import APIRouter

router = APIRouter(prefix="/payment", tags=["Payment"])

@router.get("/status")
def payment_status():
    return {"status": "Payment system online"}
