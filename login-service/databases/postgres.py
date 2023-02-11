#########################################################################################
# Author: Marco Foley
# Version: 1.0
#
#
# Database - postgres connection file
#
#
#########################################################################################


# Standard Libraries
from dotenv import load_dotenv

# Third Party Libraries

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

# Local Libraries

import logging
import os


logging.basicConfig(
    filename="customer_service.log",
    format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s",
    level=logging.DEBUG,
    force=True,
)
logger = logging.getLogger(__name__)
load_dotenv()


url = f"postgresql://{os.environ['USERNAME']}:{os.environ['PASSWORD']}@{os.environ['HOST']}:{os.environ['PORT']}/{os.environ['DATABASE']}"


engine = create_engine(url, echo=True)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
