#!/usr/bin/python3
""" indexapi """
from flask import Blueprint, jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'])
def get_status():
    """status of api"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def get_stats():
    """ Retrieves the number of each objects by type """
    classes = [Amenity, City, Place, Review, State, User]
    names = ["amenities", "cities", "places", "reviews", "states", "users"]

    num_objects = {}
    for i in range(len(classes)):
        num_objects[names[i]] = storage.count(classes[i])

    return jsonify(num_objects)
