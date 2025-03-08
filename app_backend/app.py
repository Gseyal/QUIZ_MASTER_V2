from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from application.config import config
from application.database import db
from application.model import User 
import os
from flask_cors import CORS
def createapp():
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    app.app_context().push()
    db.create_all()

app=createapp()
CORS(app)
from application.routes import *
if __name__=="__main__":
    app.run()