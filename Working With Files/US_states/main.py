import turtle
from turtle import Turtle
from scoreboard import *

import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_text = Turtle()
state_text.hideturtle()
state_text.penup()

states = pandas.read_csv("50_states.csv")
# states_dict= states.to_dict()
# states_dict["state"] = states["state"].str.lower()
# print(states_dict)
states["state"] = states["state"].str.lower()
# print(states[states.state == "arizona"]["x"].values[0])
# print(states[states['state'] == 'arizona']['x'].values[0])
tally = Scoreboard()


game_on = True
while game_on:
    user_guess = screen.textinput(title= "Guess the State", prompt= "Enter the state's name")
    for guess in states["state"]:
        if user_guess == guess and tally.score != 50 and tally.life != 0:
            x_position = (states[states.state == f"{guess}"]["x"].values[0])
            y_position = (states[states.state == f"{guess}"]["y"].values[0])
        #     # guessed_state = states[states.state == user_guess]
            state_text.goto(x_position, y_position)
            state_text.write(f"{user_guess}", move=False, align='left', font=('Arial', 8, 'normal'))
            tally.update_score()











screen.mainloop()
