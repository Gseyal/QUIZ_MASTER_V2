from application.database import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    Password = db.Column(db.String(100), nullable=False)
    role=db.Column(db.String(20),nullable=False)

class Subject(db.Model):
    __tablename__ = 'subjects'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    subject = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(1000), nullable=True)

class Chapter(db.Model):
    __tablename__ = 'chapters'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    subject = db.Column(db.String(100), unique=False, nullable=False)
    chapter = db.Column(db.String(1000), unique=True, nullable=False)

class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    subject = db.Column(db.String(100), unique=False, nullable=False)
    chapter = db.Column(db.String(1000), unique=False, nullable=False)
    question = db.Column(db.String(1000), unique=True, nullable=False)