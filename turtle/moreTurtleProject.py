#!/usr/bin/python3

from turtle import Turtle, Screen
from random import randint


# turtle = Turtle()


screen = Screen()


def etch_a_sketch(turtle, screen):
    """a mini etch a sketch game"""
    screen.listen()
    screen.onkey(lambda: turtle.forward(10), 'W')
    screen.onkey(lambda: turtle.backward(10), 'S')
    screen.onkey(lambda: turtle.left(10), 'A')
    screen.onkey(lambda: turtle.right(10), 'D')
    screen.onkey(lambda: screen.resetscreen(), 'C')
    screen.exitonclick()


def turtle_race(screen):
    """emulate a race game"""
    screen.setup(width=800, height=600)
    #turtle.bgolor('maroon')
    bet = screen.textinput(title="Make a Bet",
                           prompt="What turtle will win? Enter a color")
    if bet:
        bet = bet.lower()
        turtles = [Turtle(shape='turtle') for _ in range(6)]
        colors = ['red', 'orange', 'yellow',
                'green', 'blue', 'maroon']
        y = -250
        for i in range(6):
            turtles[i].color(colors[i])
            turtles[i].penup()
            turtles[i].setposition(x=-350, y=y)
            y += 100
        begin = True
        while begin:
            for i in turtles:
                i.forward(randint(1, 10))
                if i.xcor() >= 380:
                    print(f"You {'Win' if i.pencolor() == bet else 'Lose'}"
                          f" {i.pencolor().title()} Won")
                    begin = False
    screen.exitonclick()



turtle_race(screen)
#etch_a_sketch(turtle, screen)
