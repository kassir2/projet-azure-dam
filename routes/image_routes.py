from flask import Blueprint, jsonify, request

image_bp = Blueprint("images", __name__)

@image_bp.route("/search", methods=["GET"])
def search_images():
    query = request.args.get("q")

    return jsonify({
        "message": "API fonctionne ✅",
        "query": query,
        "images": []
    })