from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 230)
        self.score = 0
        self.hideturtle()
        self.write(f"Score: {self.score}",move= False, align = "center", font = ("Arial", 22, "normal"))
    
    def gameover(self):
        self.clear()
        self.write(f"Game Over",move= False, align = "center", font = ("Arial", 22, "normal"))
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}",move= False, align = "center", font = ("Arial", 22, "normal"))
