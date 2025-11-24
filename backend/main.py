```python
from fastapi import FastAPI
from routes.auth_routes import auth_router
from routes.community_routes import community_router
from routes.admin_routes import admin_router
from routes.ai_routes import ai_router
from routes.upload_routes import upload_router
from routes.payment_routes import payment_router
from routes.voice_routes import voice_router
from routes.analytics_routes import analytics_router
from routes.moderation_routes import moderation_router
app = FastAPI()
app.include_router(auth_router, prefix="/auth")
app.include_router(community_router, prefix="/community")
app.include_router(admin_router, prefix="/admin")
app.include_router(ai_router, prefix="/ai")
app.include_router(upload_router, prefix="/upload")
app.include_router(payment_router, prefix="/payment")
app.include_router(voice_router, prefix="/voice")
app.include_router(analytics_router, prefix="/analytics")
app.include_router(moderation_router, prefix="/moderation")
@app.get("/")
def home():
return {"status": "Backend running"}
