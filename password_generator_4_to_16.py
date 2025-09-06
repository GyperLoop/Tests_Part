#Example of a passwprd generator 
#from 4 to 16 characters
import random
import string 

def generate_password(length: int) -> str:
  if length < 4 or length > 16:
    raise ValueError()
