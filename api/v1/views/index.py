from flask import Blueprint, jsonify
from models import storage

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

@app_views.route('/status', methods=['GET'])
def get_status():
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['GET'])
def get_stats():
    stats = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User"),
    }
    return jsonify(stats)
