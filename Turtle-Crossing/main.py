#!/usr/bin/python3
"""Turtle Crossing main file"""

from turtle import Screen
from car import Car
from time import sleep
from player import Player


screen = Screen()
screen.setup(width=500, height=500)
screen.tracer(0)


Car.create_cars(start=True)

player = Player()
screen.update()

screen.listen()
screen.onkey(player.move, 'Up')

start = True
current_level = player.trackLevel.level

while start:

    start = Car.start_moving(player=player)
    if current_level < player.trackLevel.level:
        current_level += 1
        Car.increase_speed()

    sleep(0.08)
    screen.update()

screen.exitonclick()
