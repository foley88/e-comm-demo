#########################################################################################################
# 
# Author: Marco Foley
# Version: 1.0
# 
#  
# Creation of customers API Endpoints 
#
#
########################################################################################################

# FROM IMPORTS
from fastapi import APIRouter
from fastapi import Response
from fastapi import status
from fastapi import HTTPException
from fastapi import Depends
from fastapi import APIRouter
from fastapi_versioning import versioned_api_route
from passlib.context import CryptContext
from src import schemas
from database.postgres import get_db
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src import utils
from src import models

#IMPORTS
import logging
 

logger = logging.getLogger(__name__)
logging.basicConfig(filename='customer_service.log', 
                    format='%(asctime)s - %(levelname)s - %(filename)s - %(message)s', 
                    level=logging.DEBUG, force= True)


router = APIRouter(
    prefix="/customer",
    tags=['customer'],
    route_class=versioned_api_route(1, 0)
)

pass_context = CryptContext(schemes=['bcrypt'],deprecated='auto')

#create course
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_customer(customer: schemas.Customer, database: Session = Depends(get_db)):
    
    
    # adding the customer data to customer table 
    hashed_password = utils.hashpassword(customer.password)
     
    customer.password = hashed_password
    
    print(customer)
    print(customer.address.address_line_1)
    try:
        new_customer = models.Customer(id = customer.id, firstname= customer.firstname, lastname= customer.lastname,email = customer.email, password= customer.password)
        database.add(new_customer)
        database.commit()
        #adding to the address table 
        new_address = models.Address(address_line_1 = customer.address.address_line_1, 
                                 address_line_2 =customer.address.address_line_2,address_line_3 = customer.address.address_line_3, country = customer.address.country, customer_id = new_customer.id )

        database.add(new_address)    
        database.commit() 
        
    except IntegrityError:
        print("made it here")
        database.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail= f'the email: {customer.email} already exists')
        
    
        
    
            
      
    

#update Customer
@router.put("/{id}", status_code=status.HTTP_201_CREATED)
def create_customer(customer: schemas.Customer, database: Session = Depends(get_db)):
    
    
    # adding the customer data to customer table 
    hashed_password = utils.hashpassword(customer.password)
     
    customer.password = hashed_password
    
    print(customer)
    print(customer.address.address_line_1)
    try:
        new_customer = models.Customer(id = customer.id, firstname= customer.firstname, lastname= customer.lastname,email = customer.email, password= customer.password)
        database.add(new_customer)
        database.commit()
        #adding to the address table 
        new_address = models.Address(address_line_1 = customer.address.address_line_1, 
                                 address_line_2 =customer.address.address_line_2,address_line_3 = customer.address.address_line_3, country = customer.address.country, customer_id = new_customer.id )

        database.add(new_address)    
        database.commit() 
        
    except IntegrityError:
        print("made it here")
        database.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail= f'the email: {customer.email} already exists')

#delete Customer




#####items to add

# add exception handling
# update logging 
# add JWT auth 
