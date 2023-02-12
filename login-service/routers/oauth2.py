#########################################################################################################
#
# Author: Marco Foley
# Version: 1.0
#
#
# Oauth with JWT
#
#
########################################################################################################

# Standard Libraries
from datetime import datetime
from datetime import timedelta
import requests
import json
from dotenv import load_dotenv

# Third Party Libraries
from jose import JWTError
from jose import jwt
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status


# Local
from src import schemas
import os


oauth_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = "marco"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

load_dotenv()


def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()

    kid_url = f"http://localhost:8001/consumers/{os.environ['KONG_API_CONSUMER']}/jwt"
    r = requests.get(kid_url)
    kong_data = r.json()
    kid_key = kong_data["data"][0]["key"]

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, SECRET_KEY, algorithm=ALGORITHM, headers={"kid": kid_key}
    )

    return encoded_jwt


def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, algorithms=ALGORITHM, key=SECRET_KEY)

        id: str = payload.get("user_id")

        if id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=id)
        print(token_data)

    except JWTError:
        raise credentials_exception

    return token_data


# def get_current_user(token: str = Depends(oauth_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail=f"unable to validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )

#     return verify_token(token, credentials_exception)
