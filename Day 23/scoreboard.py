from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.printScore()

    def printScore(self):
        self.goto( -250, 250)
        self.write(f"Level: {self.score} ", font = FONT)
    
    def gameover(self):
        self.clear()
        self.write(f"Game Over",move= False, align = "center", font = ("Arial", 22, "normal"))
