#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

OUTPUTPATH ="Day 24/E-mails/Mail Merge Project Start/Output"

with open("Day 24/E-mails/Mail Merge Project Start/Input/Names/invited_names.txt",mode ="r") as namesFile:
    names = namesFile.readlines()

for index in range(len(names)):
    names[index] = names[index].replace("\n","")
    names[index] = names[index].strip()

with open("Day 24/E-mails/Mail Merge Project Start/Input/Letters/starting_letter.txt",mode ="r") as file:
    letter = file.read()

for name in names:
    path = OUTPUTPATH + name +".txt"
    newLetter = letter.replace("[name]", name)
    with open(path,mode ="w") as file:
        file.write(newLetter)
   
    
    







