#!/usr/bin/python3
"""Index"""
from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status")
def status():
    return jsonify({"status": "OK"})


@app_views.route("/stats")
def count():
    stats = {}
    class_names = ["Amenity", "City", "Place", "Review", "State", "User"]

    for class_name in class_names:
        stats[class_name.lower()] = storage.count(class_name)
    return jsonify(stats)
