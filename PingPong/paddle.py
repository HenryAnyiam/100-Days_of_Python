#!/usr/bin/python3

from turtle import Turtle


class Paddle(Turtle):
    """create the game pads"""

    def __init__(self, shape: str = "square",
                 undobuffersize: int = 1000,
                 visible: bool = True, user: str = "user") -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=0.8, stretch_len=4)
        self.setheading(90)
        self.placeuser(user)

    def placeuser(self, user: str) -> None:
        """place user at correct position"""
        x = 365
        if user != "user":
            x = -370
        self.setposition(x=x, y=0)

    def up(self) -> None:
        """move paddle up"""
        if self.ycor() < 250:
            self.forward(20)

    def down(self) -> None:
        """move paddle down"""
        if self.ycor() > -245:
            self.backward(20)

    def move(self) -> None:
        """move paddle"""
        if -250 < self.ycor() < 250:
            self.forward(10)
