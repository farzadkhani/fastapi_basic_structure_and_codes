from datetime import timedelta, datetime
import sys

sys.path.append("..")

from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from starlette import status

from jwt import exceptions
from jwt.utils import get_int_from_datetime

from fastapi.security import OAuth2PasswordRequestForm

import uuid

from cruds.login_cruds import login_crud
from cruds.user_cruds import user_crud
from cruds.base_user_cruds import get_active_user, get_user
from utils import deps
from schemas import account_response_schemas, account_schemas
from auth.tokens import access_token
from config import ProjectSettings
from utils.email import send_reset_password_email

router = APIRouter()


@router.post(
    "/get-token/",
    response_model=account_response_schemas.get_token_response,
    include_in_schema=False,
)
def authenticate_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(deps.session_scope),
) -> JSONResponse:
    """
    Teturn Access Token
    """
    db_user = get_active_user(email=form_data.username, db=db)
    if db_user is None:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"message": "Invalid Credentials"},
        )
    else:
        is_password_ocrrect = login_crud.check_username_password(
            email=form_data.username, password=form_data.password, db=db
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
                data={"sub": db_user.email},
                expires_delta=access_token_expires,
            )
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={
                    "access_token": token,
                    "token_type": "bearer",
                },
            )
