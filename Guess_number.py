"""
This my script to guess the number
"""
import random
from colorama import init, Fore

init(autoreset=True)

def guess_funk():
    low, high = 1, 10
    random_number = random.randint(low, high)
    try:
        user_number = int(input(Fore.GREEN + f"Guess the number (from {low} to {high}): "))
    except ValueError:
        print(Fore.RED + "Please enter a valid number.")
        raise guess_funk
    if user_number == random_number:
        print(Fore.CYAN + "You won $1!")
    else:
        hint =  "too high" if user_number > random_number else "too low"
        print(Fore.RED + f"You did`n guess right: \nHidden number: {random_number} (your guess was {hint})")

if __name__ == "__main__":
    guess_funk()