from datetime import datetime
import sys
from starlette import status

sys.path.append("..")

from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from jwt import exceptions as jwt_exceptions
# from jwt.utils import get_int_from_datetime

from app.auth.tokens import access_token
from app.data.database import session_scope, SessionLocal
from app.cruds.user_cruds import user_crud
from app.schemas.account_schemas import TokenDataSchema, UserVerifySchema
from app.logs.orm_logger import fastapi_logger
from app.config import ProjectSettings


def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=f"{ProjectSettings.API_VERSION_PATH}/getToken"
)


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(session_scope)
) -> UserVerifySchema:
    """Verify User Authentication"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    expire_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="access expired",
        headers={"WWW-Authenticate": "Bearer"},
    )
    require_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="access denied",
        headers={"WWW-Authenticate": "Bearer"},
    )
    if token:
        try:
            payload = access_token.decode_access_token(token=token)
            token_validity = payload.get("exp")
            # if get_int_from_datetime(datetime.utcnow()) >= token_validity:
            #     raise expire_exception
            email: str = payload.get("sub")
            if email is None:
                raise credentials_exception
            token_data = TokenDataSchema(email=email)
        except jwt_exceptions as e:
            fastapi_logger.exception("get_current_user")
            raise credentials_exception
        user = user_crud.verify_user(email=token_data.email, db=db)
        if user is None:
            raise credentials_exception
        return user
    else:
        raise require_exception
