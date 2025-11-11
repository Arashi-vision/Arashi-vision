from fastapi import APIRouter
from modules.ai_core import ask_ai

router = APIRouter(prefix="/ai", tags=["AI"])

@router.post("/ask")
def ai_query(query: str):
    return {"response": ask_ai(query)}
