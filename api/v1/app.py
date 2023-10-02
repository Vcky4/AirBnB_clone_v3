#!/usr/bin/python3
""" Flask app for hbnb """
from flask import Flask, make_response, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)

app.register_blueprint(app_views)


@app.errorhandler(404)
def page_not_found(error):
    """Returns JSON error repsponse"""
    return make_response(jsonify({"error": "Not found"}), 404)


@app.teardown_appcontext
def teardown(error):
    """closes storage"""
    storage.close()


if __name__ == "__main__":
    """main function"""
    host = getenv("HBNB_API_HOST", default="0.0.0.0")
    port = getenv("HBNB_API_PORT", default=5000)
    app.run(host=host, port=port, threaded=True)
