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



from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import CHAR
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.dialects .postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from database.postgres import Base
from datetime import datetime




    
class Customer(Base):
    __tablename__ = "customer"
            
    id = Column(UUID(as_uuid=True),primary_key=True, default=uuid.uuid4, nullable=False)
    firstname = Column("firstname", String, nullable=False)
    lastname =Column("lastname", String, nullable= False)
    email = Column("email", String, nullable= False,  unique=True)
    password = Column("password", String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    
 
class Address(Base):
    __tablename__= "address"  

    id = Column(Integer, primary_key=True, nullable=False)
    address_line_1 = Column("address_line_1", String, nullable = False)
    address_line_2 = Column("address_line_2",String, nullable = False)
    address_line_3 = Column("address_line_3",String, nullable = True)
    country = Column("country",String, nullable = False) 
    customer_id = Column(UUID(as_uuid=True), ForeignKey("customer.id", ondelete= "CASCADE"), nullable= False)       