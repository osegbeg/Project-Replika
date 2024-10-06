from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("blue")
endpoint = 200
kd = 0
while kd < endpoint:
    my_turtle.forward(10)
    my_turtle.penup()
    my_turtle.forward(10)
    my_turtle.pendown()
    my_turtle.forward(10)
    kd += 10






screen = Screen()
screen.exitonclick()