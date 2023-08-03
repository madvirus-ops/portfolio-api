import sys

sys.path.append("./")

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from dotenv import load_dotenv
import os

load_dotenv()
from settings import settings


Base = declarative_base()
SQLALCHEMY_DATABASE_URL = settings.DB_URL


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=False, pool_size=settings.POOL_SIZE
)
# will use alembic for database migrations
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Session:
    """ensures the database connection is always closed
    to use this we have to use fastapi.Depends() as an argument in the routes
    """
    db = SessionLocal()
    try:
        yield db

    except Exception as e:
        settings.LOGGER.error(e.args)
    finally:
        db.close()
