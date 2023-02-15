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

# standard libraries
import logging
import uuid

# third party imports
from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi_versioning import versioned_api_route
from passlib.context import CryptContext
from sqlalchemy.exc import DataError, IntegrityError
from sqlalchemy.orm import Session

# local app imports
from database.postgres import get_db
from src import models, schemas, utils

# ------------------------------------------

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename="customer_service.log",
    format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s",
    level=logging.DEBUG,
    force=True,
)


router = APIRouter(
    prefix="/customer", tags=["customer"], route_class=versioned_api_route(1, 0)
)

pass_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# create a customer registration
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_customer(customer: schemas.Customer, database: Session = Depends(get_db)):
    # adding the customer data to customer table
    hashed_password = utils.hashpassword(customer.password)

    customer.password = hashed_password

    new_id = uuid.uuid4()
    print(new_id)

    try:
        new_customer = models.Customer(
            id=new_id,
            firstname=customer.firstname,
            lastname=customer.lastname,
            email=customer.email,
            password=customer.password,
        )
        database.add(new_customer)
        database.commit()
        print("name in")
        # adding to the address table
        new_address = models.Address(
            address_line_1=customer.address.address_line_1,
            address_line_2=customer.address.address_line_2,
            address_line_3=customer.address.address_line_3,
            country=customer.address.country,
            customer_id=new_id,
        )

        database.add(new_address)
        database.commit()

        print("end")
    except IntegrityError:
        database.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"the email: {customer.email} already exists",
        )
    return {"id": new_id, "email": customer.email}


# update Customer
@router.put("/{id}", status_code=status.HTTP_201_CREATED)
def update_customer(
    id: str, dict: schemas.Update_Customer, database: Session = Depends(get_db)
):
    data = dict.dict()

    cust_query = database.query(models.Customer).filter(models.Customer.id == id)

    cust = cust_query.first()
    if cust == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"the id : {id} was not found"
        )
    else:
        try:
            cust_query.update(data)
            database.commit()
        except IntegrityError:
            database.rollback()
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"the email: {data['email']} already exists",
            )


# delete a  user
@router.delete("/{id}", status_code=status.HTTP_201_CREATED)
def delete_customer(id: str, database: Session = Depends(get_db)):
    cust_query = database.query(models.Customer).filter(models.Customer.id == id)
    cust = cust_query.first()
    if cust == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"the id : {id} was not found"
        )
    else:
        try:
            database.delete(cust)
            database.commit()
        except IntegrityError:
            pass


# error handing and testing needs to be completed
