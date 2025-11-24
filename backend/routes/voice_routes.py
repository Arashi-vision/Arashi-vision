
```python
from fastapi import APIRouter

voice_router = APIRouter()

@voice_router.post("/stt")
def stt():
    return {"stt": True}
```
