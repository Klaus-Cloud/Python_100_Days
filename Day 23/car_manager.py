
from turtle import Turtle
import random as rnd

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
X_CORD = 600

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.carList = []  
        self.startPosition =-100
        self.speed = STARTING_MOVE_DISTANCE
        
            
    def generate_Car(self):
        if 20 >= rnd.randint(0,100):
            newCar = Turtle()
            newCar.color(rnd.choice(COLORS))
            newCar.shape("square")
            newCar.penup()
            newCar.turtlesize(stretch_len = 1, stretch_wid = 2)
            newCar.ycord = rnd.randint(-250, 250)
            newCar.goto(X_CORD,newCar.ycord)
            newCar.setheading(270)
            self.carList.append(newCar)
            
    
    def cars_moving(self):
        for car in self.carList:
            new_x = car.xcor() - self.speed
            car.goto(new_x, car.ycord)
    
    def increase_speed(self):
        self.speed += MOVE_INCREMENT

    

    





