from turtle import Turtle


PACE = 20


class Paddle(Turtle):
    def __init__(self, placement):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid= 5, stretch_len=1)
        self.penup()
        self.setposition(placement)
        self.x, self.y = placement

    def up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)
