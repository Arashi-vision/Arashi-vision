

from fastapi import APIRouter

payment_router = APIRouter()

@payment_router.post("/create")
def create_payment():
    return {"payment": "created"}


