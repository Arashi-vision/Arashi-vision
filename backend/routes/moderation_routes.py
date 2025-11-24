```python
from fastapi import APIRouter

moderation_router = APIRouter()

@moderation_router.post("/scan")
def scan():
    return {"scan": "ok"}
```
