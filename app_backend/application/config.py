import os

current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
print(current_dir)

class Config:
    DEBUG = True
    SQLITE_DB_DIR = os.path.join(current_dir, "database")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(SQLITE_DB_DIR, "data.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = Config()
print(config.SQLITE_DB_DIR)