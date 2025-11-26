# ==========================================
#  Omnicore Backend - Production Main File
#  Framework: Flask
#  Supports: CORS, Security, Blueprints, AI
# ==========================================

from flask import Flask, jsonify
from flask_cors import CORS

# -----------------------------
# Initialize App
# -----------------------------
app = Flask(__name__)
CORS(app)

# -----------------------------
# Import Blueprints (Safe Mode)
# -----------------------------
try:
    from routes.auth_routes import auth_bp
    from routes.user_routes import user_bp
    from routes.post_routes import post_bp
    from routes.community_routes import community_bp
    from routes.ai_routes import ai_bp
    from routes.upload_routes import upload_bp
    from routes.notification_routes import notification_bp
    from routes.analytics_routes import analytics_bp
    from routes.public_api_routes import public_bp
except Exception as e:
    print("\n[ROUTER IMPORT ERROR] =>", e, "\n")


# -----------------------------
# Register Blueprints
# -----------------------------
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(user_bp, url_prefix="/user")
app.register_blueprint(post_bp, url_prefix="/post")
app.register_blueprint(community_bp, url_prefix="/community")
app.register_blueprint(ai_bp, url_prefix="/ai")
app.register_blueprint(upload_bp, url_prefix="/upload")
app.register_blueprint(notification_bp, url_prefix="/notifications")
app.register_blueprint(analytics_bp, url_prefix="/analytics")
app.register_blueprint(public_bp, url_prefix="/public")


# -----------------------------
# Security Headers (Middleware)
# -----------------------------
try:
    from utils.security_headers import add_headers
    @app.after_request
    def apply_headers(response):
        return add_headers(response)
except:
    print("[WARNING] Security headers not applied (file missing)")


# -----------------------------
# Error Logging Middleware
# -----------------------------
try:
    from utils.error_logger import log_error

    @app.errorhandler(Exception)
    def handle_error(e):
        log_error(str(e))
        return jsonify({"error": "Internal Server Error"}), 500
except:
    print("[WARNING] Error logger missing")


# -----------------------------
# Simple Health Check Route
# -----------------------------
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "Backend Running Successfully 🚀",
        "version": "1.0.0",
        "server": "Flask",
        "engine": "Omnicore Stable Core",
        "message": "Everything is working fine."
    })


# -----------------------------
# Run Server
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
