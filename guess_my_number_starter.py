"""
File: guessmynumber.py
----------------------
This program checks if a user's guess of a number matches that guessed by the computer
"""

import random
# use code below  to generate a random integer between 30 and 50 for example
number = (random.randint(1, 99))
# print(number)
# ********************************** YOUR CODE GOES BELOW HERE *********************************************************

user_guess = 0
guessed_number = int(input("Guess an integer between 1 and 99: "))

while guessed_number != number:
    if guessed_number < number:
        print("Kindly guess again. Guess is too low.")
        guessed_number = int(input("Guess an integer between 1 and 99: "))
        user_guess += 1
    elif guessed_number > number:
        print("Kindly guess again. Guess is too high")
        guessed_number = int(input("Guess an integer between 1 and 99: "))
        user_guess += 1

print("Congratulations on your correct guess")
