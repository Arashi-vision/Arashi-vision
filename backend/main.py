from flask import Flask
from flask_cors import CORS

# -----------------------------
# Initialize App
# -----------------------------
app = Flask(__name__)
CORS(app)

# -----------------------------
# Import Blueprints (Routers)
# -----------------------------
auth_bp = None
community_bp = None
admin_bp = None
ai_bp = None
upload_bp = None

try:
    from routes.auth_routes import auth_bp
    from routes.community_routes import community_bp
    from routes.admin_routes import admin_bp
    from routes.ai_routes import ai_bp
    from routes.upload_routes import upload_bp
except Exception as e:
    print("Error importing routes:", e)

# -----------------------------
# Register Blueprints SAFELY
# -----------------------------
if auth_bp:
    app.register_blueprint(auth_bp, url_prefix="/auth")

if community_bp:
    app.register_blueprint(community_bp, url_prefix="/community")

if admin_bp:
    app.register_blueprint(admin_bp, url_prefix="/admin")

if ai_bp:
    app.register_blueprint(ai_bp, url_prefix="/ai")

if upload_bp:
    app.register_blueprint(upload_bp, url_prefix="/upload")

# -----------------------------
# Home Route
# -----------------------------
@app.route("/", methods=["GET"])
def home():
    return {"status": "Backend Running Successfully", "version": "1.0.0"}

# -----------------------------
# Run App Locally
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)



from routes.notification_routes import router as notify_router
app.include_router(notify_router)
