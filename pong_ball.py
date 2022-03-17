from turtle import Turtle
import random

MOVE_DIST = 20


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1.5, 1.5)
        self.penup()
        self.color("white")
        #self.setheading(random.randint(0, 360))
        self.setheading(60)
        self.speed(1)

    def move(self):
        self.forward(MOVE_DIST)
