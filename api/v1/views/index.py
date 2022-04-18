#!/usr/bin/python3
""" status of api"""
from api.v1.views import app_views
from models import storage
from flask import jsonify


@app_views.route('/status')
def response():
    """ get status ok
    """
    dic = {"status": "OK"}
    return jsonify(dic)


@app_views.route('/stats')
def class_counter():
    """ get a dictionary from count method
    """
    dic = {}
    dic["amenities"] = storage.count("Amenity")
    dic["cities"] = storage.count("City")
    dic["places"] = storage.count("Place")
    dic["reviews"] = storage.count("Review")
    dic["states"] = storage.count("State")
    dic["users"] = storage.count("User")
    return jsonify(dic)


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieves the number of each objects by type """
    classes = [Amenity, City, Place, Review, State, User]
    names = ["amenities", "cities", "places", "reviews", "states", "users"]

    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])

    return jsonify(num_objs)
