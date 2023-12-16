#!/usr/bin/python3


from random import randint

from art import logo


def run_game(attempt, number):
    """start game"""
    fail = False

    print(f"You have {attempt} attempts. Start...")
    while attempt > 0:
        guess = input("Make your guess: ")
        try:
            guess = int(guess)
        except ValueError:
            print("Incorrect Guess")
            attempt -= 0
        else:
            if (guess > number) and (attempt != 0):
                print("Guess Too High, Guess Again")
            elif (guess < number) and (attempt != 0):
                print("Guess Too Low, Guess Again")
            elif (guess == number):
                print("Correct")
                fail, attempt = (True, 0)
        if fail is False:
            attempt -= 1
            print("You have"
                  f" {attempt if attempt != 0 else 'no'} attempts left")
    if fail is False:
        print(f"The number is {number}")


def number_guess():
    """run number guessing game"""

    attempt = 0
    pick = 3
    number = randint(1, 100)
    print("I'm thinking of a number between 1 and 100")
    while pick > 0:
        level = input("Choose difficulty: (easy/ hard): ").lower()
        if level == "easy":
            attempt = 10
            break
        elif level == "hard":
            attempt = 5
            break
        else:
            pick -= 1
    if attempt != 0:
        run_game(attempt, number)


if __name__ == "__main__":
    print(logo)
    print("Welcome to the Number Guessing Game")
    game = True
    while game:
        number_guess()
        if input("Restart Game (y/n): ") != 'y':
            game = False
