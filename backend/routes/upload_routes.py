```python
from fastapi import APIRouter, UploadFile

upload_router = APIRouter()

@upload_router.post("/file")
def upload(file: UploadFile):
    return {"filename": file.filename}
```
