import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
dataDict = data.to_dict('split')
NATO_Dictionary = {list[0]:list[1] for list in dataDict['data'] } # dictionary comprehension

while True:
    word = input("Enter a word:").upper()
    list_letters = [letter for letter in word]

    try:
        list_Codes = [NATO_Dictionary[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(list_Codes)
        break


