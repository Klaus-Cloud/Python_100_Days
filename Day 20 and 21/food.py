from turtle import Turtle
import random as rnd
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len =0.5 , stretch_wid = 0.5 )
        self.penup()
        x_cord = rnd.randint(-250, 250)
        y_cord = rnd.randint(-250, 250)
        self.goto(x_cord, y_cord)

    def respawn(self):
        x_cord = rnd.randint(-250, 250)
        y_cord = rnd.randint(-250, 250)
        self.goto(x_cord, y_cord)
