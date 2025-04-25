from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from application.config import config
from application.database import db
from application.model import * 
import os
from flask_cors import CORS
from flask_security import Security, SQLAlchemyUserDatastore
from application.model import User, Role
from datetime import datetime


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    with app.app_context():
        db.create_all()        
    return app

app = create_app()

datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, datastore)
CORS(app)

from application.routes import register_routes
register_routes(app)
if __name__ == "__main__":
    app.run()