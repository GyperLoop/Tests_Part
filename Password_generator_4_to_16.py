#Example of a password generator 
#from 4 to 16 characters
#also checks if the generated password is valid by the criteria
import random
import string
import re 

def generate_password(length: int) -> str:
  if length < 4 or length > 16:
    raise ValueError("Password length must be between 4 and 16 characters.")
  letters = string.ascii_letters    # a-z, A-Z
  digits = string.digits              # 0-9
  symbols = string.punctuation         # special characters
  all_characters = letters + digits + symbols
  password = [random.choice(letters), random.choice(digits), random.choice(symbols)]
  password += random.choices(all_characters, k=length - 3)
  random.shuffle(password)
  return ''.join(password)

def is_valid_password(password):
    pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{4,16}$'
    return bool(re.match(pattern, password))


if __name__ == "__main__":
  try:
    length = int(input("Enter the desired password length (4-16): "))
    password = generate_password(length)
    print(f"Generated password: \n\t{password}")
    print(f"Your password is valid: \n\t-->{is_valid_password(password)}<--")
  except ValueError as ve:
    print("Error:", ve)