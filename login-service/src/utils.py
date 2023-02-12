#########################################################################################################
#
# Author: Marco Foley
# Version: 1.0
#
#
# The utils file contains all utilities functions
#
#
########################################################################################################


from passlib.context import CryptContext

pass_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hashpassword(p: str):
    return pass_context.hash(p)


def verify_password(plain_password: str, hashed_password: str):
    return pass_context.verify(plain_password, hashed_password)
