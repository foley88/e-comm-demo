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




from pydantic import BaseModel, EmailStr, ValidationError, validator
from datetime import datetime
from datetime import date
from uuid import uuid4, UUID
from sqlmodel import Field

class Address(BaseModel):
    address_line_1: str
    address_line_2: str
    address_line_3: str = None
    country: str 
    


class Customer(BaseModel):
    id : UUID = Field(default_factory=uuid4)
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
    
   
