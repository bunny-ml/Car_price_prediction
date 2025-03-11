from flask_app.app import app
from flask import jsonify

def handler(event, context):
    return jsonify({"message": "Flask app is running!"})
