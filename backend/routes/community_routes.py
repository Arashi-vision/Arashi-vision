```python
from fastapi import APIRouter
community_router = APIRouter()
@community_router.get("/feed")
def feed():
return {"feed": []}
