import random
#insert the logos and data -Done
from art import logo, vs
from game_data import data
print(logo)

#Function: generates second, but different number
dataSize=len(data)
LASTINDEX=dataSize-1
def secondNumber(num1):
    num2= random.randint(0,LASTINDEX)
    while num2== num1:
        num2= random.randint(0,LASTINDEX)
    return num2


    
# generates a random number -Done
index1=random.randint(0,LASTINDEX)

# generates second, but different number -Done
index2=secondNumber(index1)

player =0
gameOver = False
while not gameOver:
    # generates second, but different number -Done
    index2=secondNumber(index1)
    # prints the question -Done
    name1=data[index1]["name"]
    description1  = data[index1]["description"]
    place1 = data[index1]['country']
    name2=data[index2]["name"]
    description2  = data[index2]["description"]
    place2 = data[index2]['country']

    print(f" Compare A: {name1}, {description1  }, from {place1} ")
    print(vs)
    print(f" Against B: {name2}, {description2  }, from {place2} ")

    #analyse the answer -Done
    if data[index1]['description'] > data[index2]['description']:
        correctAswer ='a'
    else:
        correctAswer ='b'

    ans =input("Who has more followers? Type 'A' or 'B':").lower()

    if correctAswer == ans :
        player +=1
        print(f"You're right! Current score: {player}")
        index1=index2
    else:
        print(f"Sorry, that's wrong. Final score:{player} ")
        gameOver=True

