"""
File: khansole_academy.py
-------------------------
Khansole Academy is a program that teaches users how to add by asking users to input answers for the addition of two
randomly generating integers between 10 and 99 inclusive. The program returns feedback based on the User's answers.

"""

# Import the random library
import random

# Initialise correct answers count to zero
correct_answers = 0

# For fun. Just to print name in the end
user_name = input("Kindly input your name to begin: ")

# Setting the loop to infinity
while True:
    # Setting the range for the random numbers
    a = random.randint(10, 99)
    b = random.randint(10, 99)
    # Storing the answer to the question
    answer = a + b

    # Presenting the question to the user
    print(f"What is {a} + {b}")

    # Taking the user input
    user_answer = int(input())

    # validate the users input if it is right or wrong
    if user_answer == answer:
        print(f"Your answer is {user_answer}")
        # To count the correct answers
        correct_answers += 1
        print(f"Correct!!! You have {correct_answers} corrects in a row")
    else:
        print(f"Your answer is {user_answer}")
        # To make the correct answers zero when one wrong is achieved
        correct_answers = correct_answers - correct_answers
        print(f"Incorrect. You have {correct_answers} corrects in a row")

    # Validate if the correct answers in a row is 3 to end the game
    if correct_answers == 3:
        print(f"Congrats {user_name}!!! You have mastered addition")

        # To escape the loop
        break
