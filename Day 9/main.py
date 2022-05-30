gameOver=False
dictionary={}
while not gameOver:
    name =input("What is your name?\n")
    bid = int(input("What´s your bid?\n"))
    dictionary[name]=bid
    otherBidders= input("Are there any other bidders?(Yes/no)\n").lower()
    if otherBidders.lower() =="no":
        gameOver=True
winnerBid=0
winner=""

for bidder in dictionary:
    if dictionary[bidder] > winnerBid:
        winnerBid =dictionary[bidder]
        winner =bidder
print(f"The winner {winner} bid ${dictionary[winner]}")  
#key=""   
# winner= max(dictionary, key=dictionary.get)
# print(f"The winner {winner} bid ${dictionary[winner]}")