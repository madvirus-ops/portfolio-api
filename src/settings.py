import sys
sys.path.append("./")


import os
from dotenv import load_dotenv
load_dotenv()
import logging
from passlib.context import CryptContext


if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(filename='logs/portfolio.log', level=logging.INFO,
                    format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Settings:
    APP_TITLE = "Edwin Ayabie - Portfolio"
    APP_DESCRIPTION="My portfolio with rest_api and graphql"
    ALLOWED_HOST = os.getenv("ALLOWED_HOST").split(",")
    SECRET_KEY = os.getenv("SECRET_KEY")
    DEBUG = bool(os.getenv("DEBUG"))
    LOGGER=logger
    POOL_SIZE = os.getenv("DB_POOL_SIZE")
    ALLOWED_PORT = int(os.getenv("PORT"))
    DB_URL = os.getenv("SQLALCHEMY_DATABASE_URL")
    TEST_DB_URL = os.getenv("SQLALCHEMY_TEST_DATABASE_URL")
    ACCESS_TOKEN_EXPIRY_TIME = 60 * 30
    REFRESH_TOKEN_EXPIRY_TIME = 60 * 24 * 365
    PASSWORD_HASHER = CryptContext(schemes=["bcrypt"], deprecated="auto")
    JWT_ALGORITHM = "HS256"
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = os.getenv("REDIS_PORT", "6379")
    PAGE_SIZE = 50


settings = Settings()