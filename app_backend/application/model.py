
from application.database import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer,nullable=False)
