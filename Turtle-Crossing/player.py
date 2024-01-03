#!/usr/bin/python3
"""Build a player"""


from turtle import Turtle
from level import Level


class Player(Turtle):
    """build a player to play the
    turtle crossing game"""

    def __init__(self, shape: str = "turtle",
                 undobuffersize: int = 1000,
                 visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.setposition(0, -230)
        self.trackLevel = Level()

    def move(self) -> None:
        """move turtle up"""
        self.forward(10)
        if self.ycor() >= 240:
            self.reset_player()

    def reset_player(self) -> None:
        """reset player to start position"""
        self.hideturtle()
        self.setposition(0, -230)
        self.showturtle()
        self.trackLevel.write_level()
