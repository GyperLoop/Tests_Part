#Example of a password generator 
#from 4 to 16 characters
#also checks if the generated password is valid by the criteria
import secrets
import string
import re 

def generate_password(length: int) -> str:
  if length < 4 or length > 16:
    raise ValueError("Password length must be between 4 and 16 characters.")
  LETTERS = string.ascii_letters    # a-z, A-Z
  DIGITS = string.digits              # 0-9
  SYMBOLS = string.punctuation         # special characters
  ALL_CHARACTERS = LETTERS + DIGITS + SYMBOLS
  password = [secrets.choice(LETTERS), secrets.choice(DIGITS), secrets.choice(SYMBOLS)]
  password += [secrets.choice(ALL_CHARACTERS) for _ in range(length - 3)]
  secrets.SystemRandom().shuffle(password)
  return ''.join(password)

def is_valid_password(password):
    pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{4,16}$'
    return bool(re.fullmatch(pattern, password))


if __name__ == "__main__":
  try:
    length = int(input("Enter the desired password length (4-16): "))
    password = generate_password(length)
    print(f"Generated password: \n\t{password}")
    print(f"Your password is valid: \n\t-->{is_valid_password(password)}<--")
  except ValueError as ve:
    print("Error:", ve)