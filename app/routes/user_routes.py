import sys

sys.path.append("..")

from enum import Enum

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.utils import deps
from app.schemas import account_response_schemas, account_schemas, redis_schemas
from app.cruds.user_cruds import user_crud
from app.cruds.login_cruds import login_crud
from app.cruds.base_user_cruds import get_user  # , get_active_user

from starlette import status

router = APIRouter()


class UserStatusEnum(str, Enum):
    enable = "enable"
    disable = "disable"


@router.post(
    "/register-regular-user/",
    responses=account_response_schemas.single_users_responses,
)
def register_regular_user(
    user: account_schemas.RegularUserCreateSchema,
    db: Session = Depends(deps.get_db),
    # current_user: account_schemas.UserVerifySchema = Depends(
    #     deps.get_current_user
    # ),
) -> JSONResponse:
    """
    Register User
    """
    db_user = get_user(email=user.email, db=db)
    if db_user is not None:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": "Email already registered"},
        )
        # raise HTTPException(
        #     status_code=status.HTTP_400_BAD_REQUEST,
        #     detail="Email already registered",
        # )
    db_user = user_crud.create_regular_user(db=db, user=user)
    if db_user is None:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Internal Server Error"},
        )
    jsonable_encoder_response = jsonable_encoder(db_user)
    del jsonable_encoder_response["password"]
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder_response,
    )
