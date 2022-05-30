from mimetypes import init
from turtle import Turtle

UP =90
DOWN = 270
class Paddle(Turtle):
    def __init__(self, xcord, ycord ):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.turtlesize( stretch_len = 5, stretch_wid = 1)
        self.goto(xcord , ycord)
        self.setheading(UP)
    
    def up(self):
        self.forward(50)
    
    def down(self):
        self.backward(50)

    