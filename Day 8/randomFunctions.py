from data import alphabet
def encrypt(text,shift):
    textList = list(text)
    for i in range(len(textList)):
        indexAlphabet=alphabet.index(textList[i]) +shift
        while indexAlphabet >= len(alphabet):
          indexAlphabet=indexAlphabet -len(alphabet)
        textList[i]=alphabet[indexAlphabet]
    print("".join(textList))

def decrypt(text,shift):
    textList = list(text)
    for i in range(len(textList)):
        indexAlphabet=alphabet.index(textList[i]) - shift
        while indexAlphabet < 0:
          indexAlphabet=indexAlphabet +len(alphabet)
        textList[i]=alphabet[indexAlphabet]
    print("".join(textList))