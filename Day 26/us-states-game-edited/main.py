from turtle import Turtle, Screen
import turtle
import pandas as pd
from states import States

screen = Screen()
screen.title("US States")
image_Path = "Day 25/us-states-game-start/blank_states_img.gif"
data_path = "Day 25/us-states-game-start/50_states.csv"
stateText = States()

screen.addshape(image_Path)
turtle.shape(image_Path)
data = pd.read_csv(data_path)


guessedStates = []
allStates = data["state"].to_list()

while len(guessedStates) < 50:
    user_Answer = screen.textinput(title= "Guess a US state's name", prompt="Write down the US state's Name:").lower()
    if user_Answer.lower() == "exit":
        outputData = pd.DataFrame([state for state in allStates if state not in guessedStates])
        outputData.to_csv("Day 25/us-states-game-start/notguessedStates.csv")
        break
    for state in allStates:
        if state.lower() == user_Answer:
            stateRow = data[data.state == state]
            xcord = int(stateRow.x)
            ycord = int(stateRow.y)
            stateText.createText(xcord, ycord, str(state))
            guessedStates.append(state)
    






screen.exitonclick()
