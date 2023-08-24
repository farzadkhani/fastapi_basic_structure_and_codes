from typing import Any
import sys

sys.path.append("..")

from sqlalchemy.orm import Session
from sqlalchemy.orm import defer
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import expression

# from data.database import session_scope
# from models import pagination
from app.models import account_models
from app.logs.orm_logger import fastapi_logger


def get_user(email: str, db: Session) -> Any:
    """Get User Data based on email"""
    try:
        data = (
            db.query(account_models.UserModel)
            .filter(account_models.UserModel.email == email)
            .options(defer(account_models.UserModel.password))
            .first()
        )
        return data
    except SQLAlchemyError as e:
        fastapi_logger.exception("get_user")
        return None


def get_active_user_by_username(username: str, db: Session) -> Any:
    """Get User Data based on username and active status"""
    try:
        data = (
            db.query(account_models.UserModel)
            .filter(
                account_models.UserModel.username == username,
                account_models.UserModel.is_active == expression.true(),
            )
            .options(defer(account_models.UserModel.password))
            .first()
        )
        return data
    except SQLAlchemyError as e:
        fastapi_logger.exception("get_user")
        return None


def get_active_user_by_email(email: str, db: Session) -> Any:
    """Get User Data based on email and active status"""
    try:
        data = (
            db.query(account_models.UserModel)
            .filter(
                account_models.UserModel.email == email,
                account_models.UserModel.is_active == expression.true(),
            )
            .options(defer(account_models.UserModel.password))
            .first()
        )
        return data
    except SQLAlchemyError as e:
        fastapi_logger.exception("get_user")
        return None
