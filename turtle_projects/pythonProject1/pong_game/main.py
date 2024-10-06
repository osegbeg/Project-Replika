import turtle, time
from turtle import Screen
from paddle import *
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=1200, height = 700)
turtle.bgcolor("black")
turtle.title("Pong Game")
screen.tracer(0)


r_paddle = Paddle((580, 0))
l_paddle = Paddle((-580, 0))
top_wall = Paddle((0, 350))
top_wall.shapesize(stretch_wid=0.5, stretch_len=1200)
# top_wall.hideturtle()
bt_wall = Paddle((0, -350))
bt_wall.shapesize(stretch_wid=0.5, stretch_len=1200)
# bt_wall.hideturtle()
ball = Ball()
scoreboard = Scoreboard()




screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_on = True
while game_on:
    ball.move()
    screen.update()

    # Detect collision with wall
    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.xcor() >= 570 and ball.distance(r_paddle) < 50 or ball.xcor() <= -570 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    # Detect paddle miss the ball
    if ball.xcor() > 570:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_scoreboard()


    if ball.xcor() < -570:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update_scoreboard()
























screen.exitonclick()