#from turtle import Turtle, Screen # from turtle import *: imports everything and then write foward (100)
import turtle as t
import random as rnd
import colorgram
def movement(turtle,colorList):
    loop = 10
    steps = 50 
    for i in range(loop):
        turtle.forward(steps)
        turtle.pencolor(rnd.choice(colorList)) 
        turtle.dot()
    turtle.backward(loop*steps)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)

path = r"C:\Users\nikla\Desktop\Python\Day 1\Day 18\image.jpg"
colors = colorgram.extract(path,100)
rgbList =[]
for element in colors: 
    rgbList.append(element.rgb) 


tim = t.Turtle()
tim.shape("turtle")
tim.color("deep sky blue")
t.colormode(255)
tim.pensize(10)
#tim.speed("fastest")
tim.penup()

tim.setheading(270)
tim.forward(300)
tim.setheading(0)


for i in range (10):
    movement(tim, rgbList)
    


screen =t.Screen()
screen.exitonclick()
