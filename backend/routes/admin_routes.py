from flask import Blueprint, request, jsonify

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/dashboard", methods=["GET"])
def get_dashboard():
    return jsonify({"message": "Admin dashboard"}), 200

@admin_bp.route("/users", methods=["GET"])
def get_users():
    return jsonify({"users": []}), 200

@admin_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    return jsonify({"message": f"User {user_id} deleted"}), 200
