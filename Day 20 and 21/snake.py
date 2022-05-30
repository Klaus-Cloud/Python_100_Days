from tkinter import NW
from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.turtleList = []
        for i in range(3):
            self.turtleList.append(Turtle(shape = "square"))
            self.turtleList[i].color("white")
            self.turtleList[i].penup()
            self.turtleList[i].goto(x = -20*i, y = 0)
            
    def add_segment(self):
        newTurtle = Turtle(shape = "square")
        newTurtle.color("white")
        newTurtle.penup()
        newTurtle.goto(self.turtleList[-1].position())
        self.turtleList.append(newTurtle)

    def move(self):
        for segment_num in range(len(self.turtleList)-1,  0,  -1):
            self.turtleList[segment_num].goto(self.turtleList[segment_num-1].pos())
        self.turtleList[0].forward(20)
    def up(self):
        if self.turtleList[0].heading() != DOWN:
            self.turtleList[0].setheading(UP)
    def down(self):
        if self.turtleList[0].heading() != UP:
            self.turtleList[0].setheading(DOWN)
    def right(self):
        if self.turtleList[0].heading() != LEFT:
            self.turtleList[0].setheading(RIGHT)
    def left(self):
        if self.turtleList[0].heading() != RIGHT:
            self.turtleList[0].setheading(LEFT)