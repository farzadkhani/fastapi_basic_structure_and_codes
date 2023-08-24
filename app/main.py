import uvicorn
import sys

sys.path.append("..")

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from app.data.database import Base, engine

# from app import config

from app.config import ProjectSettings

project_settings = ProjectSettings()


app = FastAPI(
    debug=project_settings.DEBUG,
    title=project_settings.PROJECT_NAME,
    description=project_settings.PROJECT_DESCRIPTION,
    version=project_settings.API_VERSION,
    docs_url=project_settings.DOCS_URL,
    redoc_url=project_settings.REDOC_URL,
    openapi_url=project_settings.OPENAPI_URL,
)


# Middleware Settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=ProjectSettings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Server startup event
@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)


# import all routes to eccute them
from app.routes import user_routes, login_routes


# Root API
# @app.get(ProjectSettings.API_VERSION_PATH, include_in_schema=False)
# def root() -> JSONResponse:
#     return JSONResponse(
#         status_code=200, content={"message": "Welcome to Sample Server"}
#     )


# include all routes
app.include_router(user_routes.router, prefix="/api/v1/users", tags=["users"])
app.include_router(login_routes.router, prefix="/api/v1/login", tags=["login"])


# for run admin.py routes import it to hear


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")
