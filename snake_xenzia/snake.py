#!/usr/bin/python3
"""Creating a snake class"""

from turtle import Turtle


class Snake:
    """handle the snake"""

    __turtles = [Turtle(shape='square') for _ in range(3)]

    def __init__(self) -> None:
        self.length = 2
        x = 0
        for i in self.__turtles:
            self.set_position(i, x, 0)
            x -= 20
        self.head = self.__turtles[0]
        self.head.color('red')

    def set_position(self, turtle, x, y):
        """places the snake body in
        its starting position"""
        turtle.resizemode('user')
        turtle.shapesize(0.5, 0.5, 1)
        turtle.penup()
        turtle.color('white')
        turtle.speed('slowest')
        turtle.setposition(x=x, y=y)

    def extend(self):
        """Extend snake"""
        heading = self.head.heading()
        ycor = self.__turtles[-1].ycor()
        xcor = self.__turtles[-1].xcor()
        new = Turtle(shape="square")
        if heading == 90 or heading == 270:
            self.set_position(new, xcor, (ycor - 20))
        elif heading == 180 or heading == 0:
            self.set_position(new, (xcor - 20), ycor)
        self.__turtles.append(new)
        self.length += 1

    def move(self):
        """Move the snake body  appropriately"""
        for i in range(self.length, 0, -1):
            position = (self.__turtles[i - 1].xcor(),
                        self.__turtles[i - 1].ycor())
            self.__turtles[i].setpos(position)
        self.__turtles[0].forward(10)
        if self.__turtles[0].xcor() >= 300:
            self.__turtles[0].setx(-290)
        elif self.__turtles[0].xcor() <= -300:
            self.__turtles[0].setx(290)
        elif self.__turtles[0].ycor() >= 300:
            self.__turtles[0].sety(-290)
        elif self.__turtles[0].ycor() <= -300:
            self.__turtles[0].sety(290)

    def collide(self):
        """detect head to body collission"""
        i = 1
        while i <= self.length:
            if self.head.distance(self.__turtles[i]) < 1:
                return True
            i += 1
        return False

    def up(self):
        """move up"""
        if self.__turtles[0].heading() != 270:
            self.__turtles[0].setheading(90)
            self.move()

    def down(self):
        """move down"""
        if self.__turtles[0].heading() != 90:
            self.__turtles[0].setheading(270)
            self.move()

    def left(self):
        """move left"""
        if self.__turtles[0].heading() != 0:
            self.__turtles[0].setheading(180)
            self.move()

    def right(self):
        """move right"""
        if self.__turtles[0].heading() != 180:
            self.__turtles[0].setheading(0)
            self.move()
