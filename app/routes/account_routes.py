import app

from ..schemas.account_schemas import UserSchema


@app.post("/users/")
async def create_user(user: UserSchema):
    """
    Create a new user
    """
    return {"message": "Create a new user"}
