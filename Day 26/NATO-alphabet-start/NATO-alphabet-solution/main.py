# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
import pandas as pd

data = pd.read_csv("Day 26/NATO-alphabet-start/NATO-alphabet-solution/nato_phonetic_alphabet.csv")
dataDict = data.to_dict('split')
NATO_Dictionary = {list[0]:list[1] for list in dataDict['data'] } # dictionary comprehension

word = input("Enter a word:").upper()
list_letters = [letter for letter in word]
#list_Codes = [value for letter in list_letters for (key,value) in NATO_Dictionary.items()  if letter == key]
list_Codes = [NATO_Dictionary[letter] for letter in word]
print(list_Codes)

