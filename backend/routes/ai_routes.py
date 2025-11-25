from flask import Blueprint, request, jsonify

ai_bp = Blueprint("ai", __name__)

@ai_bp.route("/chat", methods=["POST"])
def chat_ai():
    data = request.get_json()
    return jsonify({
        "reply": f"AI response for: {data.get('message')}"
    }), 200

@ai_bp.route("/analyze", methods=["POST"])
def analyze_data():
    data = request.get_json()
    return jsonify({
        "analysis": "Sample analysis output",
        "input": data
    }), 200

@ai_bp.route("/status", methods=["GET"])
def ai_status():
    return jsonify({"status": "AI services running"}), 200
