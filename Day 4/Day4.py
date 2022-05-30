import random
ans=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
handList =[rock, paper, scissors]
print("You")
print(handList[ans])

#computer´s turn
computer =random.randint(0,2)
print("Computer")
print(handList[computer])

if handList[ans -1] == handList[computer]:
    print("You win!")
elif handList[ans] == handList[computer-1]:
    print("Computers wins!")
else:
    print("Draw!")