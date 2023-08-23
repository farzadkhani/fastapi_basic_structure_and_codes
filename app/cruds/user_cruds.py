from datetime import datetime
from typing import Any
import sys

sys.path.append("..")

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import defer

from models import account_models, pagination
from utils import password as utils_password
from schemas import account_schemas
from logs.orm_logger import fastapi_logger

from app.models.account_models import UserModel
from app.schemas.account_schemas import UserSchema

from app.utils.password import get_password_hash


class UserCRUD:
    def create_user(self, db: Session, user: UserSchema) -> Any:
        """
        create user
        """
        try:
            hashed_password = get_password_hash(str(user.password))
            db_user = UserModel(
                username=user.username,
                email=user.email,
                password=hashed_password,
                first_name=user.first_name,
                last_name=user.last_name,
                is_active=user.is_active,
                is_superuser=user.is_superuser,
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow(),
            )
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            return db_user
        except SQLAlchemyError as e:
            fastapi_logger.exception("create_user")
            return None

    def update_user(self, db: Session, user: UserSchema) -> Any:
        """
        update user
        """
        try:
            db_user = (
                db.query(UserModel).filter(UserModel.id == user.id).first()
            )

            db_user.username = user.username
            # db_user.email = user.email
            db_user.first_name = user.first_name
            db_user.last_name = user.last_name
            db_user.is_active = user.is_active
            db_user.is_superuser = user.is_superuser
            db_user.updated_at = datetime.utcnow()

            db.commit()
            db.refresh(db_user)
            return db_user
        except SQLAlchemyError as e:
            fastapi_logger.exception("update_user")
            return None

    def check_password(self, user_id: int, password: str, db: Session) -> Any:
        """
        get user password
        """
        try:
            db_user = (
                db.query(UserModel).filter(UserModel.id == user_id).first()
            )
            return utils_password.verify_password(
                str(password), str(db_user.password)
            )
        except SQLAlchemyError as e:
            fastapi_logger.exception("check_password")
            return None

    def change_user_password(
        self, user_id: int, password: str, db: Session
    ) -> Any:
        """
        change user password
        """
        try:
            hashed_password = get_password_hash(str(password))
            db_user = (
                db.query(UserModel).filter(UserModel.id == user_id).first()
            )
            db_user.password = hashed_password
            db.commit()
            db.refresh(db_user)
            return db_user
        except SQLAlchemyError as e:
            fastapi_logger.exception("change_user_password")
            return None

    def update_user_password(
        self, email: str, password: str, db: Session
    ) -> Any:
        """
        update user password
        """
        try:
            hashed_password = get_password_hash(str(password))
            db_user = (
                db.query(UserModel).filter(UserModel.email == email).first()
            )
            db_user.password = hashed_password
            db.commit()
            db.refresh(db_user)
            return db_user
        except SQLAlchemyError as e:
            fastapi_logger.exception("update_user_password")
            return None

    def delete_user(self, user_id: int, db: Session):
        """
        delete user
        """
        try:
            db_user = (
                db.query(UserModel)
                .filter(UserModel.id == user_id)
                .first()
                .delete(db_user)
            )
            db.commit()
            return True
        except SQLAlchemyError as e:
            fastapi_logger.exception("delete_user")
            return None

    def user_update_status(self, user_id: int, status: str, db: Session):
        """
        update user status
        """
        try:
            db_user = (
                db.query(UserModel).filter(UserModel.id == user_id).first()
            )
            if status == "enable":
                db_user.is_active = True
            elif status == "disable":
                db_user.is_active = False
            db.commit()
            db.refresh(db_user)
            return db_user
        except SQLAlchemyError as e:
            fastapi_logger.exception("user_update_status")
            return None

    def verify_user(self, email: str, db: Session) -> Any:
        """
        verify user
        """
        try:
            db_user = (
                db.query(UserModel).filter(UserModel.email == email).first()
            )
            return db_user
        except SQLAlchemyError as e:
            fastapi_logger.exception("verify_user")
            return None

    def get_user_id(self, id: int, db: Session) -> Any:
        """
        get user id
        """
        try:
            db_user = (
                db.query(UserModel)
                .filter(UserModel.id == id)
                .options(defer("password"))
                .first()
            )
            return db_user
        except SQLAlchemyError as e:
            fastapi_logger.exception("get_user_id")
            return None

    def get_all_users(
        self, db: Session, page_num: int, page_size: int = 10
    ) -> Any:
        """
        get all users
        """
        try:
            users = (
                db.query(UserModel)
                .options(defer("password"))
                .order_by(UserModel.id.desc())
            )
            return pagination.paginate(
                query=users, page=page_num, page_size=page_size
            )
        except SQLAlchemyError as e:
            fastapi_logger.exception("get_all_users")
            return None
        
user_crud = UserCRUD()
