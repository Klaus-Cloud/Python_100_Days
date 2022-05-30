# def randomWalk(turtle,steps):
#     direction =[0,90,180,270,360]
#     r= rnd.randint(0,255)
#     b= rnd.randint(0,255)
#     g= rnd.randint(0,255)
#     turtle.pencolor((r, g, b))
#     turtle.right(rnd.choice(direction))
#     turtle.forward(steps)
    
# colour_List=["deep sky blue", "chartreuse", "dark orange", "magenta", "yellow", "slate blue", "blue violet"]
# for side in range(3,11):
#     tim.pencolor(rnd.choice(colour_List))
#     for turns in range(side):
#         tim.forward(100)
#         tim.right(360/side)

# def random_color(turtle):
#     r= rnd.randint(0,255)
#     b= rnd.randint(0,255)
#     g= rnd.randint(0,255)
#     turtle.pencolor((r, g, b))

for position in range(36):
    random_color(tim)
    tim.circle( 50)
    tim.setheading(tim.heading()+10)





