from sqladmin import ModelView
from ..schemas.account_schemas import UserSchema
from ..models.account_models import UserModel

from fastapi_admin.app import app as admin_app
from fastapi_admin.resources import Links


@admin_app.register
class Home(Links):
    label = "Home"
    icon = "fas fa-home"
    url = "/admin"


# class UserAdmin(ModelView, model=UserModel):
#     column_list = [
#         "id",
#         "first_name",
#         "last_name",
#         "username",
#         "email",
#         "is_active",
#     ]
