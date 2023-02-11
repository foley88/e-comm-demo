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

from jose import JWTError
from jose import jwt
from datetime import datetime
from datetime import timedelta
from src import schemas
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status


oauth_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = "marco"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

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


def get_current_user(token: str = Depends(oauth_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"unable to validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return verify_token(token, credentials_exception)
