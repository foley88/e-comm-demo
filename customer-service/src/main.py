######################################################################################### 
# Author: Marco Foley
# Version: 1.0
# 
#  
# Main file of the customer service
#
#
#########################################################################################

#importing the lib requierd 
from routers import customer
from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.postgres import SessionLocal
from database.postgres import engine
from database.postgres import Base
from src import models


import uvicorn
import logging
import os

logging.basicConfig(filename='customer_service.log', 
format='%(asctime)s - %(levelname)s - %(filename)s - %(message)s', 
level=logging.DEBUG, force= True)


logger = logging.getLogger(__name__)
logger.info("Customer Service started")

## create the app 

tags_metadata = [
    {
        "name": "Customer Service",
        "description": "management of customers",
    }
]

app = FastAPI(title="Customer Service",openapi_tags=tags_metadata)


models.Base.metadata.create_all(bind=engine)


#origins set to a default of all for demo purpose. adding test
origins = ["*"]

app.add_middleware(CORSMiddleware,
    allow_origins = origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

    )


app.include_router(customer.router)
# app.include_router(holes.router)


app =VersionedFastAPI(
    app = app,
    version_format="{major}.{minor}",
    prefix_format="/v{major}_{minor}"


)


if __name__ == "__main__":
    uvicorn.run(app,log_level="info")
