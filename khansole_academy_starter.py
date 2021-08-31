"""
File: khansole_academy.py
-------------------------
Khansole Academy is a program that teaches users how to add by asking users to input answers for the addition of two
randomly generating integers between 10 and 99 inclusive. The program returns feedback based on the User's answers.

"""

import random
# use code below  to generate a random integer between 30 and 50 for example
# print(random.randint(10, 99))

# ********************************** YOUR CODE GOES BELOW HERE *********************************************************
a = random.randint(10, 99)
b = random.randint(10, 99)
c = a + b
d = True
guesses = 1
user_answer = int(input(f"What is {a} + {b}? "))

while user_answer != c:
    if user_answer != c:
        print(f"Your answer is {user_answer}. Correct answer is {c}")
        user_answer = int(input(f"What is {a} + {b}? "))
        guesses = guesses + 1
    elif user_answer == c:
        print("Correct")
    break
