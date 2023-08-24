from datetime import timedelta, datetime
from typing import Annotated
import sys

sys.path.append("..")

from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from starlette import status

# from jwt import exceptions
# from jwt.utils import get_int_from_datetime

from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Form

import uuid

from app.cruds.login_cruds import login_crud
from app.cruds.user_cruds import user_crud
from app.cruds.base_user_cruds import get_active_user_by_email  # , get_user
from app.utils import deps
from app.schemas import account_response_schemas, account_schemas
from app.auth.tokens import access_token
from app.config import ProjectSettings
from app.utils.email import send_reset_password_email

router = APIRouter()


@router.post(
    "/get-token/",
    responses=account_response_schemas.get_token_response,
    include_in_schema=True,
)
def get_jwt_token(
    # form_data: OAuth2PasswordRequestForm = Depends(),
    login_info: account_schemas.GetTokenSchema,
    db: Session = Depends(deps.get_db),
) -> JSONResponse:
    """
    Teturn Access Token
    """
    db_user = get_active_user_by_email(email=login_info.email, db=db)
    if db_user is None:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"message": "Invalid Credentials"},
        )
    else:
        is_password_ocrrect = login_crud.check_email_password(
            email=login_info.email, password=login_info.password, db=db
        )
        if is_password_ocrrect is False:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"message": "Invalid Credentials"},
            )
        else:
            access_token_expires = timedelta(
                minutes=ProjectSettings.ACCESS_TOKEN_EXPIRE_MINUTES
            )
            token = access_token.create_access_token(
                data={"email": db_user.email},
                expires_delta=access_token_expires,
            )
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={
                    "access_token": token,
                    "token_type": "bearer",
                },
            )


@router.post(
    "/login-with-email-and-password/",
    responses=account_response_schemas.login_response,
    include_in_schema=True,
)
def login_user_with_email_and_password(
    user: account_schemas.UserLogInSchema,
    db: Session = Depends(deps.get_db),
) -> JSONResponse:
    """
    Login user and return access token
    """

    db_user = get_active_user_by_email(email=user.email, db=db)
    if db_user is None:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"message": "Invalid Credentials"},
        )
    else:
        is_password_ocrrect = login_crud.check_email_password(
            email=user.email, password=user.password, db=db
        )
        if is_password_ocrrect is False:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"message": "Invalid Credentials"},
            )
        else:
            uid = str(uuid.uuid4().hex)
            login_crud.login_user(user=user, session_id=uid, db=db)
            access_token_expires = timedelta(
                minutes=ProjectSettings.ACCESS_TOKEN_EXPIRE_MINUTES
            )
            token = access_token.create_access_token(
                data={"email": db_user.email},
                expires_delta=access_token_expires,
            )
            jsonable_encoder_response = jsonable_encoder(db_user)
            del jsonable_encoder_response["password"]
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={
                    "access_token": token,
                    "token_type": "bearer",
                    "session_id": uid,
                    "user": jsonable_encoder_response,
                },
            )
