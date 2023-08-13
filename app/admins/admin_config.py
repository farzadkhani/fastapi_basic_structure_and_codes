import aioredis
import os

import app

from fastapi_admin.app import app as admin_app
from fastapi_admin.providers.login import UsernamePasswordProvider

from app.models.account_models import UserModel
from app.config import BASE_DIR

login_provider = UsernamePasswordProvider(
    admin_model=UserModel,
    enable_captcha=True,
    login_logo_url="https://preview.tabler.io/static/logo.svg",
)


@app.on_event("startup")
async def startup():
    redis = await aioredis.create_redis_pool(
        "redis://localhost", encoding="utf8"
    )
    admin_app.configure(
        logo_url="https://preview.tabler.io/static/logo-white.svg",
        template_folders=[os.path.join(BASE_DIR, "templates")],
        providers=[login_provider],
        redis=redis,
    )
