from flask import Blueprint, request, jsonify

community_bp = Blueprint("community", __name__)

# Get all community posts
@community_bp.route("/posts", methods=["GET"])
def get_posts():
    return jsonify({"message": "All community posts"}), 200

# Create a new community post
@community_bp.route("/posts", methods=["POST"])
def create_post():
    data = request.get_json()
    return jsonify({"message": "Post created", "data": data}), 201

# Like a post
@community_bp.route("/posts/<int:post_id>/like", methods=["POST"])
def like_post(post_id):
    return jsonify({"message": f"Post {post_id} liked"}), 200
