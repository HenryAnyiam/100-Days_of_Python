#!/usr/bin/python3
"""score handler"""


from turtle import Turtle


class ScoreBoard(Turtle):
    """Keep track of scores"""

    def __init__(self, shape: str = "classic",
                 undobuffersize: int = 1000,
                 visible: bool = True, user: str = "user") -> None:
        super().__init__(shape, undobuffersize, visible)
        self.hideturtle()
        self.score = 0
        self.pencolor('white')
        self.place_score(user)

    def write_score(self) -> None:
        self.clear()
        self.write(arg=self.score,
                   move=False,
                   align='center',
                   font=('Arial', 30, 'normal'))

    def place_score(self, user: str) -> None:
        """place score according to user"""
        x = 200
        if user != "user":
            x = -200
        self.penup()
        self.setposition(x, 260)
        self.pendown()
        self.write_score()
