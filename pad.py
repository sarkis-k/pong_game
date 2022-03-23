from turtle import Turtle

RIGHT_POS = (560, 0)
LEFT_POS = (-560, 0)
MOVE_DIST = 20


class Pad(Turtle):
    def __init__(self, side):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        if side == "left":
            self.goto(LEFT_POS)
        else:
            self.goto(RIGHT_POS)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(), self.ycor() + -20)

