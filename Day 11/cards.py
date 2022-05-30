import random
def randomCard():
    """ It chooses a random card"""
    cards =[11, 2, 3, 4, 5,6,7,8,9,10,10,10,10]
    return random.choice(cards)
def dealersTurn(List):
    """ Dealer´s turn"""
    while sum(List) < 17:
        List.append(randomCard())
def winner(playersList, dealersList):
    if sum(playersList) > sum(dealersList):
        print("You win!")
    elif sum(playersList) < sum(dealersList):
        print("You Lose!")
    else:
        print("Draw!")
def more21beginner(List):
    if 11 in List and sum(List) >21:
        List.remove(11)
        List.append(1)
functions = {
    "Random Card": randomCard,
    "Dealer": dealersTurn,
    "Winner":winner,
    "More than 21": more21beginner,
}