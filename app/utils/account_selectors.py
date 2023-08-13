from sqlalchemy.orm import Session

from models.account_models import UserModel


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
