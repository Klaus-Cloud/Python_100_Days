import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
############ First try
# nr_letters= 3
# nr_symbols = 4
# nr_numbers = 5

# totalChar= nr_letters + nr_numbers + nr_symbols
# ans =[]


# for i in range(1,totalChar + 1): # random.shuffle
#     letterList=["L","N","S"]
#     numberList= [nr_letters,nr_numbers, nr_symbols]
    
#     options =[]
#     for j in range(0,len(numberList)):
#         if numberList[j] != 0:
#             options.append(letterList[j]) 
#     choice=options[random.randint(0,len(options)-1)]
    
#     if choice =="L":
#         ans.append(random.choice(letters)) #ans.append(letters[random.randint(0,len(letters)-1)])
#         nr_letters -=1
#     elif  choice =="N":
#         ans.append(random.choice(numbers))
#         nr_numbers -=1
#     elif choice =="S":
#         ans.append(random.choice(symbols))
#         nr_symbols -=1

# print(''.join(ans))


################# Other way
result =[]
for i in range(0,nr_letters):
    result.append(random.choice(letters))

for i in range(0,nr_symbols):
    result.append(random.choice(symbols))

for i in range(0,nr_numbers):
    result.append(random.choice(numbers))


random.shuffle(result)

print(''.join(result))
