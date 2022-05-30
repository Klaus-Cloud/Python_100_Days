from turtle import Turtle

class States (Turtle):
    def __init__(self):
        super().__init__()

    def createText(self,xcord, ycord, stateName):
        newState = Turtle()
        newState.penup()
        newState.hideturtle()
        newState.goto(xcord,ycord)
        newState.write(stateName)
