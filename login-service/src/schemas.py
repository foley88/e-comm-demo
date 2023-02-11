from pydantic import BaseModel, EmailStr, ValidationError, validator


class LoginBase(BaseModel):
    email: EmailStr
    password: str


class Login(LoginBase):
    pass


class LoginResponse(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str
