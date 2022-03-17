from turtle import Screen
from pong_ball import Ball
from pad import Pad
import time

screen = Screen()
screen.setup(width=1200, height=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

game_is_on = True

ball = Ball()
l_pad = Pad("left")
r_pad = Pad("right")

screen.listen()
screen.onkey(l_pad.up, "w")
screen.onkey(l_pad.down, "s")
screen.onkey(r_pad.up, "Up")
screen.onkey(r_pad.down, "Down")


while game_is_on:
    screen.update()
    # time.sleep(0.1)
    ball.move()

    # collision with wall
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()

    # collision with pads
    if ball.distance(r_pad) < 50 :
        ball.bounce_x()
        print("some")

    # collision with goal
    if ball.xcor() > 590:
        # score to left
        pass
    if ball.xcor() < -590:
        # score to right
        pass




game_is_on = False



screen.exitonclick()
