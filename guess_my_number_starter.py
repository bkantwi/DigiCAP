"""
File: guessmynumber.py
----------------------
This program checks if a user's guess of a number matches that guessed by the computer
"""

# import random library
import random
number = (random.randint(1, 99))

# setting guess count to 0
user_guess = 0

# User input guess number
guessed_number = int(input("Guess an integer between 1 and 99: "))

# loop to check if users guess is greater or less than the random number
while guessed_number != number:
    if guessed_number < number:
        print("Kindly guess again. Guess is too low.")
        guessed_number = int(input("Guess an integer between 1 and 99: "))
        user_guess += 1
    elif guessed_number > number:
        print("Kindly guess again. Guess is too high")
        guessed_number = int(input("Guess an integer between 1 and 99: "))
        user_guess += 1

# Print if user has got the correct guess
print("Congratulations on your correct guess")
