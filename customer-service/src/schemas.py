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


class Address(BaseModel):
    address_line_1: str
    address_line_2: str
    address_line_3: str = None
    country: str 
    


class Customer(BaseModel):
    firstname: str
    surname: str
    email: EmailStr
    dob: date
    address: Address
    
    class Config:
        orm_mode = True

class CustomerResponse(BaseModel):
    firstname:str
    surname: str
    email: EmailStr
    class Config:
        orm_mode = True
    
   
