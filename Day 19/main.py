from turtle import Turtle, Screen
import random as rnd


screen = Screen()
screen.setup(width=500, height= 400)
user_bet= screen.textinput(title ="make your bet", prompt=" Which turtle will win the race? Enter a colour:")
colours = ["red", "orange" , "yellow" , "green" ,"blue" , "purple"]
is_race_on = False

turtlelist =[]
for i in range(6):
    turtlelist.append(Turtle(shape ="turtle"))
    turtlelist[i].penup()
    turtlelist[i].color(colours[i])
    turtlelist[i].goto(x=-230, y= -125 +45*i)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtlelist:
        turtle.forward(rnd.randint(0,10))
        if turtle.xcor() == 230 :
            is_race_on = False
            winner =turtle.pencolor()

print(f"The winner is {winner}")
if winner == user_bet:
    print("You win")
else:
    print("you lose")


screen.exitonclick()