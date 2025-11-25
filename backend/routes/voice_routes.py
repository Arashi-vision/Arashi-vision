from flask import Blueprint, request, jsonify

voice_bp = Blueprint("voice_bp", __name__)

@voice_bp.route("/process", methods=["POST"])
def process_voice():
    data = request.get_json()

    text = data.get("text", "")

    return jsonify({
        "processed_text": text.upper()
    })
