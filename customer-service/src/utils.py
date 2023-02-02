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

pass_context = CryptContext(schemes=['bcrypt'],deprecated='auto')

def hashpassword(p:str):
    
    hashed_pwd = pass_context.hash(p)

    return hashed_pwd


def check_password(plain_password, hashed_password):
    return pass_context.verify(plain_password, hashed_password)

