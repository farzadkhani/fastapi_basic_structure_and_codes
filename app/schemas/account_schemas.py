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


class RegularUserCreateSchema(UserBaseSchema):
    """
    Regular User Create Schema
    """

    password: str
    first_name: str
    last_name: str
    # is_active: bool = True
    # is_staff: bool = False
    # is_superuser: bool = False
    # created_at: Optional[str] = None
    # updated_at: Optional[str] = None


class StaffUserCreateSchema(UserBaseSchema):
    """
    Staff User Create Schema
    """

    password: str
    first_name: str
    last_name: str
    is_staff: bool = True
    # is_active: bool = True
    # is_superuser: bool = False
    # created_at: Optional[str] = None
    # updated_at: Optional[str] = None


class SuperUserCreateSchema(UserBaseSchema):
    """
    Super User Create Schema
    """

    password: str
    first_name: str
    last_name: str
    is_staff: bool = True
    is_superuser: bool = True
    # is_active: bool = True
    # created_at: Optional[str] = None
    # updated_at: Optional[str] = None


class RegularUserUpdateSchema(UserBaseSchema):
    """
    Regular User Update Schema
    """

    first_name: str
    last_name: str
    # is_staff: bool = False
    # is_superuser: bool = False
    # is_active: bool = True
    # updated_at: Optional[str] = None


class StaffUserUpdateSchema(UserBaseSchema):
    """
    Staff User Update Schema
    """

    first_name: str
    last_name: str
    is_staff: bool = True
    # is_superuser: bool = False
    # is_active: bool = True
    # updated_at: Optional[str] = None


class SuperUserUpdateSchema(UserBaseSchema):
    """
    Super User Update Schema
    """

    first_name: str
    last_name: str
    is_staff: bool = True
    is_superuser: bool = True
    # is_active: bool = True
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

    email: str
    password: str
    ip_address: str
    browser: str


class RegularUserSchema(RegularUserCreateSchema):
    """
    User Schema
    """

    id: int

    class Config:
        orm_mode = True
        # from_attributes = True


class GetTokenSchema(BaseModel):
    """
    loging schemas: get token
    """

    email: str
    password: str


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
