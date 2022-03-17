from turtle import Turtle

RIGHT_POS = (560, 0)
LEFT_POS = (-560, 0)
MOVE_DIST = 20


class Pad(Turtle):
    def __init__(self, side):
        super().__init__()
        self.pad = Turtle()
        self.create_pad(side)

    def create_pad(self, side):
        self.pad.color("white")
        self.pad.shape("square")
        self.pad.penup()
        self.pad.shapesize(stretch_wid=5, stretch_len=1)
        if side == "left":
            self.pad.goto(LEFT_POS)
        else:
            self.pad.goto(RIGHT_POS)

    def up(self):
        self.pad.goto(self.pad.xcor(), self.pad.ycor() + 20)

    def down(self):
        self.pad.goto(self.pad.xcor(), self.pad.ycor() + -20)

