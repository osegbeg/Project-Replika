import turtle
from turtle import Turtle, Screen
import colorgram, random

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.hideturtle()
turtle.colormode(255)
color = colorgram.extract('hirst_image.jpg', 30)
# print(color)
color_list = []

for i in range(len(color)):
    rgb = color[i].rgb
    red = rgb.r
    green = rgb.g
    blue = rgb.b
    colors = (red, green, blue)
    color_list.append(colors)
# print(color_list)

def draw_row():
    dot_count = 0
    while dot_count < 10:
        my_turtle.dot(20, random.choice(color_list))
        my_turtle.penup()
        my_turtle.forward(50)
        dot_count += 1


for i in range(-200, 300, 50):
    my_turtle.penup()
    my_turtle.setposition(-400, -600)
    my_turtle.sety(i)
    draw_row()

# draw_row()


screen = Screen()
screen.exitonclick()