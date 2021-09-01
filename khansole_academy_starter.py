"""
File: khansole_academy.py
-------------------------
Khansole Academy is a program that teaches users how to add by asking users to input answers for the addition of two
randomly generating integers between 10 and 99 inclusive. The program returns feedback based on the User's answers.

"""

import random
# use code below  to generate a random integer between 30 and 50 for example
# print(random.randint(10, 99))
correct_answers = 0
# ********************************** YOUR CODE GOES BELOW HERE *********************************************************
while True:
    a = random.randint(10, 99)
    b = random.randint(10, 99)

    print("What is " + str(a) + " plus " + str(b) + "?")
    user_answer = int(input())

    if user_answer == (a+b):
        print("Correct")
        correct_answers += 1
    else:
        print("Incorrect. The answer is " + str(a+b))
        correct_answers = correct_answers -correct_answers

    print("Player has " + str(correct_answers) + " points")

    if correct_answers == 3:
        print("Congrats. You have mastered addition")
        break
