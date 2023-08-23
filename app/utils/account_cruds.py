from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.models.account_models import UserModel
from app.schemas.account_schemas import UserSchema

from app.utils.password import get_password_hash


class UserRepository:
    def create_user(self, db: Session, user: UserSchema):
        try:
            hashed_password = get_password_hash(str(user.password))
            db_user = UserModel(
                username=user.username,
                password=hashed_password,
                email=user.email,
                first_name=user.first_name,
                last_name=user.last_name,
            )
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            return db_user
        except SQLAlchemyError as e:
            # TODO: log error
            # fastapi_logger.exception("create_user")
            return None


def retrieve_all_users(db: Session):
    """
    Retrieve all users
    """
    return db.query(UserModel).all()


def retrieve_user_by_id(db: Session, user_id: int):
    """
    Retrieve user by id
    """
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def retrieve_user_by_username(db: Session, username: str):
    """
    Retrieve user by username
    """
    return db.query(UserModel).filter(UserModel.username == username).first()


def post_user(db: Session, user: UserModel):
    """
    Create new user
    """
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
