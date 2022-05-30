import random
from cards import functions
def playGame():
    gameOver =False
    player=[]
    dealer=[]
    for i in range(2):
        player.append(functions["Random Card"]())
        dealer.append(functions["Random Card"]())

    functions["More than 21"](player)
    functions["More than 21"](dealer)

    print(f"Player: {player} Sum:{sum(player)}")
    print(f"Dealer: {dealer[0]}")   

    while not gameOver:
        playersWill = input("Would like to pick up a new card?(y/n)\n").lower()
        if playersWill == "n":
            gameOver =True
        else:
            player.append(functions["Random Card"]())
            print(f"Player: {player} Sum:{sum(player)}")
            if sum(player) > 21:
                gameOver =True

    if sum(player) > 21:
        print("You lose!")
    else:
        functions["Dealer"](dealer)
        print(f"Dealer: {dealer} Sum:{sum(dealer)}") 
        if sum(dealer) > 21:
            print("You win")
        else:
            functions["Winner"](player,dealer)
while input("Do you want play a game of BlackJack? Type 'y' or 'n':").lower() == "y":
    playGame()

