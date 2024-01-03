#!/usr/bin/python3
"""Car module"""


from turtle import Turtle
from random import choice, randint
from typing import List
from player import Player


class Car(Turtle):
    """handle car creation and methods"""

    Colors = ["red", "blue", "yellow",
              "orange", "maroon", "pink"]
    Gone: List = []
    Cars: List = []
    Car_Speed = 5

    def __init__(self, x: int, y: int, shape: str = "square",
                 undobuffersize: int = 1000,
                 visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.color(choice(type(self).Colors))
        self.shapesize(stretch_len=2)
        self.setposition(x=x, y=y)

    def move(self, speed: int = 0) -> None:
        """move car"""
        speed = speed if speed else Car.Car_Speed
        self.backward(speed)

    @classmethod
    def create_cars(cls, start: bool = False) -> List:
        """generate cars"""
        total = len(cls.Gone)
        xpos = (250, 251)
        if start:
            total = randint(10, 15)
            xpos = (-240, 240)
        if cls.Gone:
            for i in cls.Gone:
                cls.Cars.remove(i)
        for _ in range(total):
            cls.Cars.append(cls(randint(*xpos), randint(-200, 200)))
        return cls.Cars

    @classmethod
    def start_moving(cls, player: Player) -> bool:
        """start moving cars across the screen"""
        for i in cls.Cars:
            i.move()
            if i.distance(player) <= 20:
                cls.game_over()
                return False
            if i.xcor() < -250 and i not in cls.Gone:
                i.move(100)
                cls.Gone.append(i)

        if cls.Gone:
            cls.create_cars()
            cls.Gone.clear()
        return True

    @classmethod
    def game_over(cls) -> None:
        """End current game"""
        writer = Turtle()
        writer.hideturtle()
        writer.write(arg="GAME OVER",
                     move=False,
                     align='center',
                     font=('Arial', 15, 'normal'))

    @classmethod
    def increase_speed(cls) -> None:
        """Increase Car speed"""
        cls.Car_Speed += 5
