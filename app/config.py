import os
import json
from pathlib import Path
from typing import Dict

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# def get_config() -> Dict:
#     """Get Config Json"""
#     with open(
#         str(Path(__file__).parent.parent)
#         + os.sep
#         + "conf"
#         + os.sep
#         + "conf.json",
#         "r",
#     ) as fp:
#         return json.load(fp)


# class EmailSettings:
#     """ Email Settings"""
#     __DATA = get_config()['EMAIL_CONF']
#     EMAIL_RESET_TOKEN_EXPIRE_HOURS = __DATA["EMAIL_RESET_TOKEN_EXPIRE_HOURS"]
#     EMAIL_ID = __DATA["EMAIL_ID"]
#     EMAIL_PASSWORD = __DATA["EMAIL_PASSWORD"]
#     SMTP_SERVER = __DATA["SMTP_SERVER"]
#     SMTP_PORT = __DATA["SMTP_PORT"]


# class DBSettings:
#     """ Database Configuration"""
#     __DATA = get_config()['DATABASE_CONF']
#     # 'postgres+psycopg2://USER:PASSWORD@localhost:5432/DATABASE'
#     SQLALCHEMY_DATABASE_URL = __DATA["DATABASE"] + '+' + __DATA[
#         "POSTGRES_ADAPTER"] + '://' + \
#                               __DATA["POSTGRES_USER"] + ':' + __DATA[
#                                   "POSTGRES_PASSWORD"] + '@' + __DATA[
#                                   "POSTGRES_SERVER"] + ':' + \
#                               __DATA["POSTGRES_PORT"] + '/' + __DATA[
#                                   "POSTGRES_DB"]


# class ProjectSettings:
#     """Project Configuration"""

#     __DATA = get_config()["PROJECT_CONF"]
#     PROJECT_NAME = __DATA["PROJECT_NAME"]
#     PROJECT_DESCRIPTION = __DATA["PROJECT_DESCRIPTION"]
#     API_VERSION = __DATA["API_VERSION"]
#     API_VERSION_PATH = __DATA["API_VERSION_PATH"]
#     SERVER_NAME = __DATA["SERVER_NAME"]
#     SERVER_HOST = __DATA["SERVER_HOST"]
#     BACKEND_CORS_ORIGINS = __DATA["BACKEND_CORS_ORIGINS"]
#     ACCESS_TOKEN_EXPIRE_MINUTES = __DATA["ACCESS_TOKEN_EXPIRE_MINUTES"]
#     SESSION_TOKEN_EXPIRE_SECONDS = __DATA["SESSION_TOKEN_EXPIRE_SECONDS"]


## FastAPI config
DEBUG = True

## DB config
SQLALCHEMY_DATABASE_URL = "sqlite:///./db.sqlite3"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
CHECK_SAME_THREAD = False
AUTOCOMMIT = False
AUTOFLUSH = False

## JWT config
