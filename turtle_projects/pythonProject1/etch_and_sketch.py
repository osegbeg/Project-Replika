from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()
screen.listen()

def forward_key():
    tom.forward(10)

def backward_key():
    tom.backward(10)

def counter_clockwise_key():
    tom.left(10)

def clockwise_key():
    tom.right(10)


def clear():
    tom.penup()
    tom.clear()
    tom.home()
    tom.pendown()

screen.onkey(fun=forward_key, key= 'w')
screen.onkey(fun=backward_key, key= 's')
screen.onkey(fun=counter_clockwise_key, key= 'a')
screen.onkey(fun=clockwise_key, key= 'd')
screen.onkey(fun=clear, key= 'c')

screen.exitonclick()