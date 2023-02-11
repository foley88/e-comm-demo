#########################################################################################################
#
# Author: Marco Foley
# Version: 1.0
#
#
# Login - main app file
#
#
########################################################################################################

# Stanard libraries
import logging

# Third Party Libraries
from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI
from fastapi.middleware.cors import CORSMiddleware


# Local Libraries

from routers import login

# ---------------------------------------------

logging.basicConfig(
    filename="loginservice.log",
    format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s",
    level=logging.DEBUG,
    force=True,
)
logger = logging.getLogger(__name__)
logger.info("Login service started")

## create the app

tags_metadata = [
    {
        "name": "login",
        "description": "allows the user to login and get a token",
    }
]

app = FastAPI(title="login service", openapi_tags=tags_metadata)

# origins set to a default of all for demo purpose. adding test
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(login.router)


app = VersionedFastAPI(
    app=app, version_format="{major}.{minor}", prefix_format="/v{major}_{minor}"
)
