import os
from datetime import timedelta, datetime
from typing import Dict
from pathlib import Path
import sys

sys.path.append("..")

# from jwt import (
#     JWT,
#     jwk_from_pem,
# )
# from jwt.utils import get_int_from_datetime
import jwt

from app.config import EmailSettings, AuthenticationSettings


def get_app_directory_path() -> str:
    return str(Path(__file__).parent.parent) + "/"


class AccessToken:
    """Access Token Util Class"""

    def __init__(self):
        self.__SECRET_KEY = AuthenticationSettings.SECRET_KEY
        self.__ALGORITHM = AuthenticationSettings.ALGORITHM

    def create_access_token(
        self, *, data: dict, expires_delta: timedelta = None
    ) -> str:
        """Create Access Token Using JWT"""

        key = self.__SECRET_KEY
        algorithm = self.__ALGORITHM
        data["exp"] = datetime.utcnow() + expires_delta

        encoded_jwt = jwt.encode(data, key, algorithm=algorithm)
        return encoded_jwt

    def decode_access_token(self, *, token: str) -> Dict:
        """Decode Access Token"""

        key = self.__SECRET_KEY
        algorithm = self.__ALGORITHM

        return jwt.decode(token, key, algorithms=[algorithm])

    def generate_password_reset_token(self, email: str) -> str:
        """Generate Access Token for password Reset email"""
        delta = timedelta(hours=EmailSettings.EMAIL_RESET_TOKEN_EXPIRE_HOURS)
        now = datetime.utcnow()
        expires = now + delta
        key = self.__SECRET_KEY
        algorithm = self.__ALGORITHM

        encoded_jwt = jwt.encode(
            {
                "exp": expires,
                "email": email,
            },
            key,
            algorithm=algorithm,
        )
        return encoded_jwt

    def verify_password_reset_token(self, token: str) -> Dict:
        """Decode Access Token"""
        key = self.__SECRET_KEY
        algorithm = self.__ALGORITHM

        return jwt.decode(token, key, algorithms=[algorithm])


access_token = AccessToken()
