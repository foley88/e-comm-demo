#########################################################################################################
#
# Author: Marco Foley
# Version: 1.0
#
#
# API Schemas
#
#
########################################################################################################


from datetime import date, datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, EmailStr, ValidationError, validator
from sqlmodel import Field


class Address(BaseModel):
    address_line_1: str
    address_line_2: str
    address_line_3: str = None
    country: str


class Customer(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    address: Address
    password: str

    class Config:
        orm_mode = True


class CustomerResponse(BaseModel):
    email: EmailStr = None

    class Config:
        orm_mode = True


class Update_Customer(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr

    class Config:
        orm_mode = True
