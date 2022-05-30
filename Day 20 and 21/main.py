import random as rnd
from tracemalloc import stop    
from turtle import  Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

myScreen = Screen ()
myScreen.setup(width =600, height = 600)
myScreen.bgcolor("black")
myScreen.title("Snake Game")
myScreen.tracer(0)

snake = Snake()
myScreen.listen()
myScreen.onkey(snake.up, "Up")
myScreen.onkey(snake.down,"Down")
myScreen.onkey(snake.left,"Left")
myScreen.onkey(snake.right,"Right")

food = Food()
scoreboard = Scoreboard()

gameOn = True

while gameOn:
    myScreen.update()
    time.sleep(0.1)
    snake.move()
    if snake.turtleList[0].distance(food) < 15 :
        food.respawn()
        scoreboard.increase_score()
        snake.add_segment()
    # collision to the wall 
    if snake.turtleList[0].xcor() > 290 or snake.turtleList[0].xcor() < - 290 or snake.turtleList[0].ycor() > 290 or snake.turtleList[0].ycor() < - 290:
        gameOn = False
        scoreboard.gameover()
    # Tail collision
    for segment in snake.turtleList[1:]:    
        if snake.turtleList[0].distance(segment) < 1 :
            gameOn = False
            scoreboard.gameover()
            







myScreen.exitonclick()