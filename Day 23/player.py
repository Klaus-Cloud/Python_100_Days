from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.reset()
        self.setheading(90)

    def reset(self):
        self.goto(STARTING_POSITION)
        self.yposition = STARTING_POSITION[1]
        self.xposition = STARTING_POSITION[0]
        
    def move(self):
        self.yposition +=  MOVE_DISTANCE
        self.goto(self.xposition, self.yposition)
    
    def sucessCondition(self):
        return self.ycor() > FINISH_LINE_Y
          

