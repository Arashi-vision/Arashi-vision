from fastapi import FastAPI
from routes import auth_routes, community_routes, admin_routes, ai_routes

app = FastAPI(title="Omnicore Backend")

app.include_router(auth_routes.router)
app.include_router(community_routes.router)
app.include_router(admin_routes.router)
app.include_router(ai_routes.router)

@app.get("/")
def root():
    return {"message": "Backend running successfully!"}
