import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
screen = Screen()
scoreboard = Scoreboard()
carmanager =CarManager()

screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.generate_Car()
    carmanager.cars_moving()
    if player.sucessCondition():
        scoreboard.score += 1
        player.reset()
        scoreboard.clear()
        scoreboard.printScore()
        carmanager.increase_speed()
    for car in carmanager.carList:
        if player.distance(car) < 10 :
            game_is_on = False
            scoreboard.gameover()
            

screen.exitonclick()