import turtle
from turtle import Turtle, Screen
import random

my_turtle = Turtle()
my_turtle.shape("turtle")
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


for i in range(0,360,10):
    my_turtle.color(random_color())
    my_turtle.circle(100)
    my_turtle.setheading(i)













screen = Screen()
screen.exitonclick()