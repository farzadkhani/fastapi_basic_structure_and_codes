from typing import List

from fastapi import APIRouter, Depends, HTTPException, status, Path

from sqlalchemy.orm import Session

from app.data.database import SessionLocal
from app.schemas.account_schemas import UserSchema
from app.utils.account_selectors import (
    retrieve_all_users,
    retrieve_user_by_id,
    retrieve_user_by_username,
    post_user,
)

api_router = APIRouter()


def get_db():
    """
    Get database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@api_router.get(
    "/users/", response_model=List[UserSchema], summary="Get all users"
)
def get_all_users(db: Session = Depends(get_db)):
    """
    Get all users
    """
    users = retrieve_all_users(db)
    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No users found",
        )
    return users


@api_router.get(
    "/users/{user_id}", response_model=UserSchema, summary="Get user by id"
)
def get_user_by_id(
    user_id: int = Path(..., gt=0),
    db: Session = Depends(get_db),
):
    """
    Get user by id
    """
    user = retrieve_user_by_id(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return user


@api_router.get(
    "/users/{username}",
    response_model=UserSchema,
    summary="Get user by username",
)
def get_user_by_username(
    username: str = Path(..., min_length=3),
    db: Session = Depends(get_db),
):
    """
    Get user by username
    """
    user = retrieve_user_by_username(db, username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return user


@api_router.post(
    "/users/", response_model=UserSchema, summary="Create a new user"
)
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    """
    Create a new user
    """
    user = post_user(db, user)
    return user
