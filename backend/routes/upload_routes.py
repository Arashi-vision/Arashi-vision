from flask import Blueprint, request, jsonify
import os

upload_bp = Blueprint("upload_bp", __name__)
UPLOAD_FOLDER = "uploads"

# Create folder if missing
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# -----------------------------
# File Upload API
# -----------------------------
@upload_bp.route("/file", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    return jsonify({
        "success": True,
        "file_name": file.filename,
        "path": file_path
    })
