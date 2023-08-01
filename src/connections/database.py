import sys
sys.path.append("./")

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from dotenv import load_dotenv
import os
load_dotenv()





Base = declarative_base()
SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")



engine = create_engine(
        SQLALCHEMY_DATABASE_URL, echo = False,pool_size=5)
#will use alembic for database migrations
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)




def get_db():
    """ ensures the database connection is always closed 
        to use this we have to use fastapi.Depends() as an argument in the routes
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()







