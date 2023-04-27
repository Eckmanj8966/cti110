# [TODO] A brief description of the project
# Date
# CTI-110 P5HW - Math Quiz
# Joshua Eckman
#
import random
num1 = random.randint(1, 99)
num2 = random.randint(1, 99)

def adding_random_numbers(num1, num2):
    answer = num1 + num2
    guess = 0
    atempts = 0
    finished = 0
    
    print(f' ', num1)
    print(f'+', num2)
    print("Enter answer.")
    guess = int(input())
    
    while finished != 1:
        if guess < answer:
            atempts += 1
            print("Sorry, guess is too low.")
            print('')
            print("Try again:", end='')
            guess = int(input())
        elif guess > answer:
            atempts += 1
            print("Sorry, guess is too high.")
            print('')
            print("Try again:", end='')
            guess = int(input())
        else:
            atempts += 1
            print("Congradulations!!! Your answer is correct.")
            print(f'Number of guesses: {atempts}')
            print('')
            finished = 1

def subtracting_random_numbers(num1, num2):
    answer = num1 - num2
    guess = 0
    atempts = 0
    finished = 0
    
    print(f' ', num1)
    print(f'-', num2)
    print("Enter answer.")
    guess = int(input())
    
    while finished != 1:
        if guess < answer:
            atempts += 1
            print("Sorry, guess is too low.")
            print('')
            print("Try again:", end='')
            guess = int(input())
        elif guess > answer:
            atempts += 1
            print("Sorry, guess is too high.")
            print('')
            print("Try again:", end='')
            guess = int(input())
        else:
            atempts += 1
            print("Congradulations!!! Your answer is correct.")
            print(f'Number of guesses: {atempts}')
            print('')
            finished = 1
    
choice = 0
while choice != 3:
    print("Welcome to Math Quiz")
    print("")
    print("")
    print("MAIN MENU")
    print("---------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
    print("")
    print("Please choose one of the menu options:", end='')
    choice = int(input())

    if choice == 1:
        adding_random_numbers(num1, num2)
    elif choice == 2:
        subtracting_random_numbers(num1, num2)
    elif choice > 3:
        print('ERROR: Incorrect Input')
        print('')
