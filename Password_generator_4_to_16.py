#Example of a passwprd generator 
#from 4 to 16 characters
import random
import string 

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

if __name__ == "__main__":
  try:
    length = int(input("Enter the desired password length (4-16): "))
    password = generate_password(length)
    print(f"Generated password: {password}")
  except ValueError as ve:
    print("Error:", ve)
