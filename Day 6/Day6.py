def turn_around():
    turn_left()
    turn_left()
def turn_right():
    turn_around()
    turn_left() 

while not at_goal():
    while wall_in_front():
        if right_is_clear():
            turn_right() 
        else:
            turn_left()
    move()
    if right_is_clear():
            turn_right()