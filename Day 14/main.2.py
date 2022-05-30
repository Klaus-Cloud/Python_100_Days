import random
#insert the logos and data -Done
from art import logo, vs
from game_data import data
print(logo)

def contestant(dict):
    accountsName = dict['name']
    accountsDescription = dict['description']
    accountsCountry = dict['country']
    return f" {accountsName}, {accountsDescription}, from {accountsCountry}"

def check(guess,afollowers,bfollowers):
    if afollowers> bfollowers:
        return guess == "a"
    else:
        return guess == "b"

accountA =random.choice(data)
score =0
gameOver = False
while not gameOver:
    accountB =random.choice(data)
    while accountA == accountB:
        accountB =random.choice(data)

    print("Compare A: " + contestant(accountA) )
    print(vs)
    print(" Against B:" + contestant(accountB))

    # if accountA['description'] > accountB['description']:
    #         correctAswer ='a'
    # else:
    #         correctAswer ='b'   
    ans =input("Who has more followers? Type 'A' or 'B':").lower()
    if check(ans,accountA['description'],accountB['description']) :
        score +=1
        print(f"You're right! Current score: {score}")
        accountA=accountB
    else:
        print(f"Sorry, that's wrong. Final score:{score} ")
        gameOver=True