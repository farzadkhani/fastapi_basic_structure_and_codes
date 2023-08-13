from fastapi import FastAPI

from . import config

app = FastAPI(
    debug=config.DEBUG,
    title="Basic structure for fastapi project",
    description="A simple project structure for fastapi project",
    version="0.1.0",
    docs_url="/swagger/docs/",
    redoc_url="/swagger/redoc/",
    openapi_url="/swagger/openapi.json",
)


# import all routes to eccute them
from .routes import account_routes

app.include_router(
    account_routes.api_router, prefix="/api/v1/account", tags=["account"]
)

# for run admin.py routes import it to hear
