#!/usr/bin/python3

from turtle import Turtle
from random import randint


class Food(Turtle):
    """Handle food"""

    def __init__(self, shape: str = "circle",
                 undobuffersize: int = 1000,
                 visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.place()

    def place(self):
        """replace food on screen"""
        x, y = (randint(-290, 290), randint(-290, 290))
        self.setposition(x, y)
