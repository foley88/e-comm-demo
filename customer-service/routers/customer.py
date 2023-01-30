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
from datetime import datetime
from pymongo.errors import ConnectionFailure
from passlib.context import CryptContext
from src import schemas

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
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.CustomerResponse)
def create_customer(customer: schemas.Customer):
    try:
        
        print(customer.firstname)

        logger.info(status.HTTP_201_CREATED)

    except ConnectionFailure:
        logger.critical("Server not available")



    return customer

#update Customer


#delete Customer




#####items to add

# add exception handling
# update logging 
# add JWT auth 
