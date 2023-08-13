from pydantic import BaseModel
from typing import Optional


class UserBaseSchema(BaseModel):
    """
    User Base Schema
    """

    username: str
    email: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class UserCreateSchema(UserBaseSchema):
    """
    User Create Schema
    """

    password: str


class UserSchema(UserCreateSchema):
    """
    User Schema
    """

    # from_attributes: ClassVar[bool] = True

    id: int
    is_active: bool

    class Config:
        orm_mode = True
        from_attributes = True
