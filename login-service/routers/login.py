#########################################################################################################
#
# Author: Marco Foley
# Version: 1.0
#
#
# Login service
#
#
########################################################################################################

# Standard Libraries
from configparser import ConfigParser
import logging


# Third Party Libraries
from fastapi import APIRouter, status, HTTPException, Response, Depends
from fastapi_versioning import versioned_api_route
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

# Local Libraries
from databases.postgres import get_db
from src.utils import verify_password
from src import models
from routers.oauth2 import create_access_token


logging.basicConfig(
    filename="loginservice.log",
    format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s",
    level=logging.DEBUG,
    force=True,
)

router = APIRouter(
    prefix="/login", tags=["Authentication"], route_class=versioned_api_route(1, 0)
)

c = ConfigParser()
c.read("/Users/marcofoley/Documents/Developtment/golfappv2/auth/app/config.ini")


# Login into the application.
@router.post("/", status_code=status.HTTP_201_CREATED)
def user_login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    database: Session = Depends(get_db),
):
    # take in username and password
    # search database for user
    # pass the plain text password and hashed password to utils for validation
    # if passed validation provide the client back a JWT token
    # if failed dont allow access
    print("Login working")
    print(form_data.__dict__)

    login_query = database.query(models.Customer).filter(
        models.Customer.email == form_data.username
    )
    user = login_query.first()

    if user == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="there was an issue with the details provided",
        )
    else:
        result = verify_password(form_data.password, user.password)

    if result == False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="there was an issue with the details provided ",
        )
    else:
        data = dict()
        data["id"] = user.id
        print(data)

    return create_access_token(data, None)
