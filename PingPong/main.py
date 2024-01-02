#!/usr/bin/python3

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Ping Pong")
screen.tracer(0)

draw = Turtle()
draw.pencolor('white')
draw.hideturtle()
draw.penup()
draw.setposition(x=0, y=-300)
draw.setheading(90)
draw.pensize(4)
for i in range(60):
    if i % 2 == 0:
        draw.pendown()
    else:
        draw.penup()
    draw.forward(10)

User = Paddle()
Computer = Paddle(user="computer")
PongBall = Ball()


computer_score = ScoreBoard(user="computer")
user_score = ScoreBoard()


def reset(scorer):
    """reset ball to starting"""
    screen.tracer(0)
    PongBall.reset()
    scorer.score += 1
    scorer.write_score()
    screen.update()
    sleep(1)
    screen.tracer(1)


screen.update()
screen.tracer(1)
screen.listen()
screen.onkey(User.up, 'Up')
screen.onkey(User.down, 'Down')
screen.onkey(Computer.up, 'w')
screen.onkey(Computer.down, 's')
PongBall.move()

game_on = True

while game_on:
    PongBall.move()
    if ((User.distance(PongBall) <= 50) and
       (PongBall.xcor() >= 350) and
       (PongBall.xcor() <= 370)):
        PongBall.bounce_off_x()

    if (Computer.distance(PongBall) <= 50
        and (PongBall.xcor() <= -350) and
       (PongBall.xcor() >= -370)):
        PongBall.bounce_off_x()
    if PongBall.xcor() > 380:
        reset(computer_score)

    if PongBall.xcor() < -380:
        reset(user_score)

    if PongBall.ycor() >= 280 or PongBall.ycor() <= -280:
        PongBall.bounce_off_y()

screen.exitonclick()
