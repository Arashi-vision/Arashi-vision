from fastapi import APIRouter

router = APIRouter(prefix="/public")

@router.get("/hello")
def hello():
    return {"msg": "Public API working"}
