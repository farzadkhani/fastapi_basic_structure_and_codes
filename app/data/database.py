import sys
sys.path.append("..")

from contextlib import contextmanager

from app import config

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# from app import config

# Create a database URL for SQLAlchemy

# Create the SQLAlchemy
# "check_same_thread": False is just for SQLite
engine = create_engine(
    config.DBSettings.SQLALCHEMY_DATABASE_URL,
    pool_size=config.DBSettings.POOL_SIZE,
    max_overflow=config.DBSettings.MAX_OVERFLOW,
    pool_recycle=config.DBSettings.POOL_RECYCLE,
    pool_pre_ping=config.DBSettings.POOL_PRE_PING,
    pool_use_lifo=config.DBSettings.POOL_USE_LIFO,
    # connect_args={"check_same_thread": config.DBSettings.CHECK_SAME_THREAD},
)

# Create a SessionLocal class
SessionLocal = sessionmaker(
    autocommit=config.DBSettings.AUTOCOMMIT,
    autoflush=config.DBSettings.AUTOFLUSH,
    bind=engine,
)

# Create a Base class
Base = declarative_base()


@contextmanager
def session_scope() -> SessionLocal:
    """Provide a transactional scope around a series of operations."""
    db = None
    try:
        db = SessionLocal()  # create session from SQLAlchemy sessionmaker
        yield db
    finally:
        db.close()