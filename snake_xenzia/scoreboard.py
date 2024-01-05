#!/usr/bin/python3


from turtle import Turtle
import json


class ScoreBoard(Turtle):
    """Keep track of scores"""

    __file = "snake.json"

    def __init__(self, shape: str = "classic",
                 undobuffersize: int = 1000,
                 visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.hideturtle()
        self.score = 0
        self.highscore = self.get_high_score()
        self.pencolor('white')
        self.penup()
        self.setposition(0, 280)
        self.pendown()
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}  "
                   f" High Score: {self.highscore}",
                   move=False,
                   align='center',
                   font=('Arial', 15, 'normal'))
    
    def get_high_score(self):
        """save high score to file"""

        try:
            with open(type(self).__file, 'r', encoding="utf-8") as my_file:
                score = json.load(my_file)
        except FileNotFoundError:
            return 0
        else:
            return score['score']

    def game_over(self):
        self.penup()
        self.setposition(0, 0)
        self.pendown()
        self.write(arg="GAME OVER",
                   move=False,
                   align='center',
                   font=('Arial', 25, 'normal'))
        if self.score > self.highscore:
            self.penup()
            self.setposition(0, -40)
            self.pendown()
            self.write(arg=f"New Highscore: {self.score}",
                       move=False,
                       align='center',
                       font=('Arial', 25, 'normal'))
            self.save_high_score()

    
    def save_high_score(self):
        """save high score to file"""
        with open(type(self).__file, 'w', encoding='utf-8') as my_file:
            json.dump({'score': self.score}, my_file)
