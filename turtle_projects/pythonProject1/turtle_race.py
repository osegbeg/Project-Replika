import turtle, random
from random import randint
from turtle import Turtle, Screen



screen = Screen()
screen.setup(width=700, height = 500)
user_bet = (turtle.textinput(title = "Enter your Bet", prompt = "Which turtle are you betting for the win")).lower()
color_pack = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
y_positions = [-90, -60, -30, 0, 30, 60, 90]
turtle_names = ["rom", "oom", "yom", "gom", "bom", "iom", "vom"]
turtle_objects = []


def prep_turtle(turtle_name, color_num):
    """
    this function prepares the turtle, it takes the name of the turtle, the color_num representing
    the rainbow colors where 0 is red and 6 is violet
    """
    turtle_name = Turtle()
    turtle_name.shape("turtle")
    turtle_name.color(color_pack[color_num])
    turtle_name.penup()
    turtle_name.goto(-330, y_positions[color_num])
    return turtle_name


for player, i in zip(turtle_names,range(7)):
    turtle_objects.append(prep_turtle(player, i))


game_on = False

if user_bet:
    game_on = True

while game_on:
    for t in turtle_objects:
        if t.xcor() >= 330:
            game_on = False
            winning_color = t.pencolor()
            if user_bet == winning_color:
                print(f"The winner is {winning_color}, you won your bet!!!!")
            else:
                print(f"The winner is {winning_color}, you lost your bet!!!!")
        stride = randint(0, 10)
        t.forward(stride)








screen.exitonclick()