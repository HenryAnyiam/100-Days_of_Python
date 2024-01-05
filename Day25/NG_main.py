#!/usr/bin/python3
"""build a us states guess game"""

from turtle import Screen, Turtle
import pandas


screen = Screen()
image = "./nigerian_map.gif"
screen.addshape(image)

turtle = Turtle(image)

writer = Turtle()
writer.hideturtle()


def write_state(x, y, text):
    """write state name on its correct point"""
    writer.penup()
    writer.setposition(x, y)
    writer.pendown()
    writer.write(f"{text}",
                 font=("Arial", 15, "normal"))


states = pandas.read_csv("./Nigerian_states.csv")
state_names = states.states.to_list()
x_axis = states.x.to_list()
y_axis = states.y.to_list()

total_states = len(state_names)

guesses = 0
guessed = []

while guesses < total_states:

    guess = screen.textinput(title=f"{guesses}/{total_states}"
                             "States Guessed Correctly",
                             prompt="Please input a state name").title()
    if guess in state_names and guess not in guessed:
        index = state_names.index(guess)
        state_x = x_axis[index]
        state_y = y_axis[index]
        guessed.append(guess)
        write_state(state_x, state_y, guess)
        guesses += 1


writer.penup()
writer.setposition(-200, 250)
writer.write(f"Congratulations, You Are A Patriotic Citizen Of Nigeria",
             font=("Arial", 20, "normal"))


screen.mainloop()
