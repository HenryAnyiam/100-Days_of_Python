#!/usr/bin/python3
"""Handle game levels"""

from turtle import Turtle


class Level(Turtle):
    """Keep track of game level"""

    def __init__(self, shape: str = "classic",
                 undobuffersize: int = 1000,
                 visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.level = 0
        self.setposition(x=-200, y=200)
        self.hideturtle()
        self.write_level()

    def write_level(self) -> None:
        """Update current level"""
        self.clear()
        self.level += 1
        self.write(arg=f"Level: {self.level}",
                   move=False,
                   align='center',
                   font=('Arial', 15, 'normal'))
