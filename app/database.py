from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from . import config

# Create a database URL for SQLAlchemy

# Create the SQLAlchemy
# "check_same_thread": False is just for SQLite
engine = create_engine(
    config.SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": config.CHECK_SAME_THREAD},
)

# Create a SessionLocal class
SessionLocal = sessionmaker(
    autocommit=config.AUTOCOMMIT,
    autoflush=config.AUTOFLUSH,
    bind=engine,
)

# Create a Base class
Base = declarative_base()
