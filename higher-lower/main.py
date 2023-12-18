#!/usr/bin/python3


from art import logo, vs
from game_data import data
from random import choice


data_length = len(data)
choices = [i for i in range(data_length)]


def start_game():
    """Start the higher or lower game"""
    print(logo)
    score = 0
    failed = False
    current_compare = choice(choices)
    choices.remove(current_compare)
    while (data_length > 1) and (not failed):
        new_compare = choice(choices)
        choices.remove(new_compare)
        first = data[current_compare]
        next = data[new_compare]
        print(f"Compare A: {first['name']}, {first['description']}, from {first['country']}.")
        print(vs)
        print(f"Against B: {next['name']}, {next['description']}, from {next['country']}.")
        answer = input("Who has more Instagram followers? (A or B): ").capitalize()
        if answer == 'A' and (first['follower_count'] > next['follower_count']):
            score += 1
        elif answer == 'B' and (first['follower_count'] < next['follower_count']):
            score += 1
        else:
            failed = True
            print("Wrong choice")
        if not failed:
            print(f"You are right, your score is {score}")
            current_compare = new_compare

    if not failed:
        print("You passed it all")


if __name__ == "__main__":
    start_game()