from pydantic import BaseModel
from typing import Optional


class UserBaseSchema(BaseModel):
    """
    User Base Schema
    """

    username: str
    email: str


class UserVerifySchema(UserBaseSchema):
    """
    User Verify Schema
    """

    id: int


class UserCreateSchema(UserBaseSchema):
    """
    User Create Schema
    """

    password: str
    first_name: str
    last_name: str
    is_active: bool = True
    is_superuser: bool = False
    # created_at: Optional[str] = None
    # updated_at: Optional[str] = None


class UserUpdateSchema(UserBaseSchema):
    """
    User Update Schema
    """

    first_name: str
    last_name: str
    is_active: bool = True
    is_superuser: bool = False
    # updated_at: Optional[str] = None


class UserChangePasswordSchema(BaseModel):
    """
    User Change Password Schema
    """

    password: str
    new_password: str


class UserResetPasswordSchema(BaseModel):
    """
    User Reset Password Schema
    """

    token: str
    password: str


class UserAuthenticateSchema(BaseModel):
    """
    User Authenticate Schema
    """

    password: str


class UserLogInSchema(BaseModel):
    """
    User LogIn Schema
    """

    account_id: str
    password: str
    ip_address: str
    browser: str


class UserSchema(UserCreateSchema):
    """
    User Schema
    """

    id: int

    class Config:
        orm_mode = True
        # from_attributes = True


class TokenSchema(BaseModel):
    """
    loging schemas: token
    """

    access_token: str
    token_type: str


class TokenDataSchema(BaseModel):
    """
    loging schemas: token date
    """

    email: str = None
    expire: str = None
    issue_time: str = None
