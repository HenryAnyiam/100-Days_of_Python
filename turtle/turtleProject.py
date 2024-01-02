#!/usr/bin/python3

from turtle import Screen, Turtle, colormode
from random import choice, randint
import colorgram

turtle = Turtle()
colormode(255)

turtle.shape("turtle")
turtle.color("red", "green")


def draw_square(turtle):
    """draw a square with the turtle"""
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)


def draw_dashed_line(turtle):
    """draw dashed line with the turtle"""
    for _ in range(15):
        turtle.forward(10)
        turtle.up()
        turtle.forward(10)
        turtle.down()


def draw_various_shapes(turtle):
    """draw poligons from 3 to 10 sided"""
    colors = ['red', 'green', 'blue',
              'orange', 'yellow', 'aquamarine',
              'pink', 'maroon']
    for i in range(3, 11):
        turn = int(360 / i)
        turtle.pencolor(colors[i - 3])
        for _ in range(i):
            turtle.forward(100)
            turtle.right(turn)


def move_random(turtle):
    """make haphazard movement with the turtle"""
    turn = [turtle.right, turtle.left]
    angle = [0, 90, 180, 360]
    move = [turtle.forward, turtle.backward]
    turtle.pensize(8)
    turtle.speed(8)
    for _ in range(200):
        colors = (randint(0, 255), randint(0, 255), randint(0, 255))
        turtle.pencolor(colors)
        choice(turn)(choice(angle))
        choice(move)(30)


def draw_spirograph(turtle, gap):
    """draw a spirograph"""
    turtle.speed(0)
    loop = int(360 / gap)
    for _ in range(loop):
        colors = (randint(0, 255), randint(0, 255), randint(0, 255))
        turtle.pencolor(colors)
        turtle.circle(100)
        turtle.left(gap)


def draw_spot(turtle):
    """draw spotted art"""
    turtle.speed(0)
    colors = colorgram.extract('image.jpeg', (18 * 32))
    colors = [tuple(i.rgb) for i in colors]
    turtle.penup()
    x = -300
    y = -270
    turtle.setpos(x, y)
    turtle.pendown()
    for _ in range(29):
        for _ in range(32):
            turtle.pencolor(choice(colors))
            turtle.dot(10)
            turtle.penup()
            turtle.forward(20)
        y += 20
        turtle.setpos(x, y)
        turtle.pendown()


draw_spot(turtle)


myScreen = Screen()

myScreen.exitonclick()
