import random
from random import randint
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
X_POSITION = 280




class CarManager:


    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        if random.randint(1,6) == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y_position = randint(-250, 250)
            new_car.goto(X_POSITION, y_position)
            self.cars.append(new_car)


    def car_move(self):
        for car in self.cars:
            car.backward(self.speed)

    def next_level(self):
        self.speed += MOVE_INCREMENT



