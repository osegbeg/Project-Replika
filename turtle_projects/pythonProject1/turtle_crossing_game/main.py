import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

tim = Player()
car = CarManager()
scores = Scoreboard()
screen.onkey(tim.player_move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.car_move()
    scores.current_score()

    for x in car.cars:
        if x.distance(tim) < 20:
            scores.game_over()
            game_is_on = False

    if tim.ycor() >= 300:
        tim.reset_position()
        scores.increment_score()
        car.next_level()









screen.exitonclick()
