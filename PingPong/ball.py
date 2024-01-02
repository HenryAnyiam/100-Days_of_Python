#!/usr/bin/python3


from turtle import Turtle


class Ball(Turtle):
    """pong ball"""

    def __init__(self, shape: str = "circle",
                 undobuffersize: int = 1000,
                 visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.color('white')
        self.speed(10)
        self.xdirection = 10
        self.ydirection = 10

    def reset(self) -> None:
        """reset to starting position"""
        self.goto(0, 0)
        self.bounce_off_x()

    def move(self) -> None:
        """move ball"""
        xcor = self.xcor() + self.xdirection
        ycor = self.ycor() + self.ydirection

        self.goto(xcor, ycor)

    def bounce_off_x(self) -> None:
        """bounce off x coordinate"""
        self.xdirection *= -1

    def bounce_off_y(self) -> None:
        """bounce off y coordinate"""
        self.ydirection *= -1
