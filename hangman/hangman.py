#!/usr/bin/python3

import random

stages = __import__("hangman_art").stages
logo = __import__("hangman_art").logo
guesses = __import__("hangman_word").word_list


lives = len(stages) - 1

guess = random.choice(guesses)
length = len(guess)

gameOver = False
blank = ['_' for i in guess]
guessed_letters = []

print(logo)
print("START!!!\n")
while ((not gameOver) and (lives >= 0)):
    print(f"\n{' '.join(blank)}\n")
    guessed = input("Guess a letter: ").lower()
    if ((len(guessed) == 1) and (guessed in guess) and (guessed not in blank)):
        guessed_letters.append(guessed)
        for i in range(length):
            if guess[i] == guessed:
                blank[i] = guessed
        if '_' not in blank:
            print(" ".join(blank))
            print("You Won")
            gameOver = True
    elif guessed in guessed_letters:
        print("This Letter has already been guessed!!!")
    else:
        guessed_letters.append(guessed)
        print("Wrong!!!")
        print(stages[lives])
        lives -= 1