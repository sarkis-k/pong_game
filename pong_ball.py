from turtle import Turtle

MOVE_DIST = 0.3


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1.5, 1.5)
        self.penup()
        self.color("white")
        self.x_move = 0.2
        self.y_move = 0.2

    def move(self):
        #self.speed(1)
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        print("here")
        self.x_move *= -1

