from data import alphabet
from randomFunctions import encrypt
from randomFunctions import decrypt
from logo import logo

# def caesar (direction,text, shift):
#     if direction == "encode":
#         encrypt(text,shift)
#     elif direction == "decode":
#         decrypt(text,shift)
def caesar (direction,text, shift):
    endText =""
    shift = shift%len(alphabet)
    if direction == "decode":
        shift *= -1
    for char in text:
        if alphabet.count(char)  > 0:
            indexAlphabet=alphabet.index(char) +shift
            while indexAlphabet >= len(alphabet):
                indexAlphabet=indexAlphabet -len(alphabet)
            endText += alphabet[indexAlphabet]
        else:
            endText +=char
    print(endText)

ans =True
print(logo)
while ans:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction,text, shift)
    choice= input(" Restart the cipher program?\n").lower()
    if choice=="no":
        ans=False
