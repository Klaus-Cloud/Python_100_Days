print("Welcome to Treasure island?\n")
ans1 =input("Left or right?")
if ans1.lower() == "left":
    ans2 =input("Swim or Wait?\n")
    if ans2.lower() == "wait":
        ans3 =input("Red or Blue or yellow?\n")
        if ans3.lower() == "yellow":
            print("You win")
        else:
            print("game over")
    else:
        print("game over")
else:
    print("game over")
