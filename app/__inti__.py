from fastapi import FastAPI

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


# for run admin.py routes import it to hear
