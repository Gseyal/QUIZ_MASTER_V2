from flask import current_app as app , jsonify,request
from application.model import *
from application.database import db
import uuid
@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"  # Allow frontend
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"  # Allowed methods
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"  # Allowed headers
    return response
@app.route("/uuid",methods=['GET'])
def info():
    return jsonify({'id':str(uuid.uuid4())})
@app.route("/message",methods=['GET'])
def get_message():
    response =jsonify({"message": "hello from port 50000"})
    return response
@app.route("/app_data",methods=['POST'])
def add_data():
    data=request.get_json()
    record=User(username=data.get('username'),age=data.get('age'))
    db.session.add(record)
    db.session.commit()
    return jsonify({"message":"Done"})

