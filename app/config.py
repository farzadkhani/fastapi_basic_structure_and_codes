import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

## FastAPI config
DEBUG = True

## DB config
SQLALCHEMY_DATABASE_URL = "sqlite:///./db.sqlite3"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
CHECK_SAME_THREAD = False
AUTOCOMMIT = False
AUTOFLUSH = False

## JWT config
