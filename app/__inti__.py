from fastapi import FastAPI
from sqladmin import Admin
from fastapi_admin.app import app as admin_app

from . import config
from .database import engine

app = FastAPI(
    debug=config.DEBUG,
    title="URL Shortener",
    description="A simple URL shortener",
    version="0.1.0",
    docs_url="/swagger/docs/",
    redoc_url="/swagger/redoc/",
    openapi_url="/swagger/openapi.json",
)


# import all routes to eccute them
from .routes import account_routes

# for run admin.py routes import it to hear
app.mount("/admin", admin_app)
