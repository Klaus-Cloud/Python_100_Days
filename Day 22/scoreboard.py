from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.scoreRight = 0
        self.scoreLeft = 0
        self.printScore()

    def printScore(self):
        self.goto(-100, 200)
        self.write(f"{self.scoreRight}", align = "center", font = ("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(f"{self.scoreLeft}", align = "center", font = ("Courier", 80, "normal"))
