import turtle
from turtle import Turtle, Screen
import random
my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.pensize(5)
my_turtle.speed(7)
turtle.colormode(255)
pace = [-30, 30]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


my_turtle.color(random_color())

# # square
# for _ in range(4):
#     my_turtle.forward(100)
#     my_turtle.right(90)
#
# # pentagon
# for _ in range(5):
#     my_turtle.forward(100)
#     my_turtle.right(72)
#
# # Hexagon
# for _ in range(6):
#     my_turtle.forward(100)
#     my_turtle.right(60)
#
# # Heptagon
# for _ in range(7):
#     my_turtle.forward(100)
#     my_turtle.right(51.42857)
#
# # Octagon
# for _ in range(8):
#     my_turtle.forward(100)
#     my_turtle.right(45)
#
# # Nonagon
# for _ in range(9):
#     my_turtle.forward(100)
#     my_turtle.right(40)
#
# # Decagon
# for _ in range(10):
#     my_turtle.forward(100)
#     my_turtle.right(36)


n = [0, 90, 180, 270]
steps = 0
while steps < 101:
    my_turtle.forward(random.choice(pace))
    my_turtle.setheading(random.choice(n))
    steps += 1
    my_turtle.color(random_color())



screen = Screen()
screen.exitonclick()