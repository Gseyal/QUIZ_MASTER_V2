import os

current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
print(current_dir)

class Config:
    DEBUG = True
    SQLITE_DB_DIR = os.path.join(current_dir, "database")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(SQLITE_DB_DIR, "data.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "supersecret"
    SECURITY_PASSWORD_SALT = "random_salt"
    SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authorization"
    SECURITY_TOKEN_MAX_AGE = 3600 #1 hour 1hr=60mins*60sec
    SECURITY_JOIN_USER_ROLES = True
    SECURITY_PASSWORD_SINGLE_HASH = False

config = Config()
print(config.SQLITE_DB_DIR)