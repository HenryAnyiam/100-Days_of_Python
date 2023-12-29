#!/usr/bin/python3


from turtle import Turtle


class ScoreBoard(Turtle):
    """Keep track of scores"""

    def __init__(self, shape: str = "classic",
                 undobuffersize: int = 1000,
                 visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.hideturtle()
        self.score = 0
        self.pencolor('white')
        self.penup()
        self.setposition(0, 280)
        self.pendown()
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}",
                   move=False,
                   align='center',
                   font=('Arial', 15, 'normal'))

    def game_over(self):
        self.penup()
        self.setposition(0, 0)
        self.pendown()
        self.write(arg="GAME OVER",
                   move=False,
                   align='center',
                   font=('Arial', 25, 'normal'))
