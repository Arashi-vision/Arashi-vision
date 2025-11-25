from flask import Blueprint, jsonify

analytics_bp = Blueprint("analytics_bp", __name__)

# -----------------------------
# Basic Analytics Data
# -----------------------------
@analytics_bp.route("/stats", methods=["GET"])
def get_stats():
    return jsonify({
        "visits": 1200,
        "active_users": 87,
        "daily_signups": 19
    })
