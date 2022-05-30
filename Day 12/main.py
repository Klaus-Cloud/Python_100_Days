import random
from logo import logo

def noMoreAttempts():
    global gameOver
    if attempts ==0:
        print("You've run out of guesses, you lose.")
        gameOver =True
def reduceAttempts ():
    global attempts
    attempts -= 1

def comparison():
    global chosenNumber
    global gameOver
    if chosenNumber == NUMBER:
        print("You  guess it!")
        gameOver =True
    elif chosenNumber > NUMBER:
        print("Too high")
        reduceAttempts ()
    elif chosenNumber < NUMBER:
        print("too low")
        reduceAttempts ()

print(logo)

options ={
    "easy":10,
    "hard":5,
}
NUMBER= random.randint(1,100)
print("Welcome to the Number Guessing Game! \n I'm thinking of a number between 1 and 100.")
gameOver =False
attempts = options[input("Choose a difficulty. Type 'easy' or 'hard':").lower()]
while not gameOver:
    print(f"You have {attempts} attempts remaining to guess the number.")
    chosenNumber= int(input("Make a guess: "))
    comparison()
    noMoreAttempts()


