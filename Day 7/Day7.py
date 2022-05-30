import random
from HangMan import hangMan 
import words
result =0
lastResult = 0
gameOver =False
image=[]
mistakeCounter =0

repeat=[]
word =list(random.choice(words.word_list))

for i in range(0,len(word)):
    image.append("_")

while result !=len(word) and not(gameOver):
    print(image)
    letter = input("Guess a letter:").lower()
    if not letter in repeat:
        result += word.count(letter)
        repeat.append(letter)

    if result >lastResult :
        for i in range(len(word)):
            if letter == word[i]:
                image[i] =letter
    else:
        hangMan(mistakeCounter)
        mistakeCounter +=1
        if mistakeCounter == 7:
            gameOver = True
    lastResult =result

if result ==len(word):
    print(image)
    print("You Win")
else:
    print("You lose!")