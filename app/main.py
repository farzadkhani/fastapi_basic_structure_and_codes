from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
from app.data.database import Base, engine

from app import config

app = FastAPI(
    debug=config.DEBUG,
    title="Basic structure for fastapi project",
    description="A simple project structure for fastapi project",
    version="0.1.0",
    docs_url="/swagger/docs/",
    redoc_url="/swagger/redoc/",
    openapi_url="/swagger/openapi.json",
)


# Server startup event
@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

# import all routes to eccute them
from .routes import account_routes


# Root API
# @app.get(ProjectSettings.API_VERSION_PATH, include_in_schema=False)
# def root() -> JSONResponse:
#     return JSONResponse(
#         status_code=200, content={"message": "Welcome to Sample Server"}
#     )


# include all routes
app.include_router(
    account_routes.api_router, prefix="/api/v1/accounts", tags=["account"]
)
# for run admin.py routes import it to hear


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000, log_level='debug')
