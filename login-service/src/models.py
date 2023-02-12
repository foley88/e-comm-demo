#########################################################################################################
#
# Author: Marco Foley
# Version: 1.0
#
#
# The file contains all orm models
# Drop any table that requires an update.
#
########################################################################################################


import uuid
from datetime import datetime

from sqlalchemy import CHAR, Column, ForeignKey, Integer, String, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from databases.postgres import Base


class Customer(Base):
    __tablename__ = "customer"

    id = Column("id", String, nullable=False, primary_key=True)
    firstname = Column("firstname", String, nullable=False)
    lastname = Column("lastname", String, nullable=False)
    email = Column("email", String, nullable=False, unique=True)
    password = Column("password", String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, nullable=False)
    address_line_1 = Column("address_line_1", String, nullable=False)
    address_line_2 = Column("address_line_2", String, nullable=False)
    address_line_3 = Column("address_line_3", String, nullable=True)
    country = Column("country", String, nullable=False)
    customer_id = Column(
        "customer_id",
        String,
        ForeignKey("customer.id", ondelete="CASCADE"),
        nullable=False,
    )
