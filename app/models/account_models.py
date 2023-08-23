from datetime import datetime

import sys
sys.path.append("..")

from app.data.database import Base
from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    Text,
    TIMESTAMP,
    PrimaryKeyConstraint,
    UniqueConstraint,
)


# Create a User model
class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(Text, nullable=False)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    is_active = Column(Boolean, nullable=False, default=True)
    is_superuser = Column(Boolean, nullable=False, default=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)

    # table configurations
    __table_args__ = (
        PrimaryKeyConstraint("id", name="users_pkey"),
        UniqueConstraint("email"),
        {"schema": "articles", "extend_existing": True},
    )

    def __repr__(self):
        # descriptive repressentational strings params
        return (
            f"<UserModel(id={self.id}, username={self.username},"
            f" email={self.email}, first_name={self.first_name},"
            f" last_name={self.last_name}, is_active={self.is_active},"
            f" is_superuser={self.is_superuser}, created_at={self.created_at},"
            f" updated_at={self.updated_at})>"
        )


class UserLogingAtemptModel(Base):
    __tablename__ = "user_login_attempts"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, index=True)
    session_id = Column(String, nullable=False)
    ip_address = Column(String, nullable=True)
    browser = Column(String, nullable=True)
    status = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)

    # table configurations
    __table_args__ = (
        PrimaryKeyConstraint("id", name="user_login_attempts_pkey"),
    )

    def __repr__(self):
        # descriptive repressentational strings params
        return (
            f"<UserLogingAtemptModel(id={self.id}, email={self.email},"
            f" session_id={self.session_id}, ip_address={self.ip_address},"
            f" browser={self.browser}, status={self.status},"
            f" created_at={self.created_at})>"
        )
