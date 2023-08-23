from typing import Any
import sys
sys.path.append("..")

from sqlalchemy.orm import Session
from sqlalchemy.orm import defer
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import expression

# from data.database import session_scope
# from models import pagination
from models import account_models
from logs.orm_logger import fastapi_logger


def get_user(email: str, db: Session) -> Any:
    """Get User Data based on email"""
    try:
        data = (
            db.query(account_models.UserModel)
            .filter(account_models.UserModel.email == email)
            .options(defer("password"))
            .first()
        )
        return data
    except SQLAlchemyError as e:
        fastapi_logger.exception("get_user")
        return None


def get_active_user(email: str, db: Session) -> Any:
    """Get User Data based on email and active status"""
    try:
        data = (
            db.query(account_models.UserModel)
            .filter(
                account_models.UserModel.email == email,
                account_models.UserModel.is_active == expression.true(),
            )
            .options(defer("password"))
            .first()
        )
        return data
    except SQLAlchemyError as e:
        fastapi_logger.exception("get_user")
        return None
