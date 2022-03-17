from turtle import Turtle

RIGHT_POS = [(560, -40), (560, -20), (560, 0), (560, 20), (560, 40)]
LEFT_POS = [(-560, -40), (-560, -20), (-560, 0), (-560, 20), (-560, 40)]
MOVE_DIST = 20
UP = 90
DOWN = 270


class Pad(Turtle):
    def __init__(self, side):
        super().__init__()
        self.pad_shape = []
        self.create_pad(side)

    def create_pad(self, side):
        if side == "left":
            self.add_bits(LEFT_POS)
        else:
            self.add_bits(RIGHT_POS)

    def add_bits(self, positions):
        for x in positions:
            pad_bit = Turtle()
            pad_bit.color("white")
            pad_bit.shape("square")
            pad_bit.penup()
            pad_bit.goto(x)
            self.pad_shape.append(pad_bit)

    def move(self, heading):
        # for bit in range(len(self.pad_shape)-1, 0, -1):
        #     new_x = self.pad_shape[bit-1].xcor()
        #     new_y = self.pad_shape[bit-1].ycor()
        #     self.pad_shape[bit].goto(new_x, new_y)
        # self.pad_shape[0].forward(MOVE_DIST)
        for bit in range(len(self.pad_shape)):
            self.pad_shape[bit].setheading(heading)
            self.pad_shape[bit].forward(MOVE_DIST)

    def up(self):
        self.move(UP)

    def down(self):
        self.move(DOWN)
