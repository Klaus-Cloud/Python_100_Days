# TO DO 1 : PRINT THE RESOURCES OF OUR MACHINE for report 
from data import MENU, resources, coins
# TO DO 3 : CHOOSE AN OPTION AND SEE IF ITS POSSIBLE
def enoughResources(choice):
    drink=MENU[choice]["ingredients"]
    for necessaryIngredients in drink:
        for realIngredients in resources:
            if necessaryIngredients ==realIngredients:
                if drink[necessaryIngredients] > resources[realIngredients][0]:
                    print(f"Sorry there is not enough {realIngredients}")
                    return False
    return True
# TO DO 5 : IS THE TRASECTION POSSIBLE?
def reduceIngredients (choice):
    drink=MENU[choice]["ingredients"]
    for necessaryIngredients in drink:
        for realIngredients in resources:
            if necessaryIngredients ==realIngredients:
                resources[realIngredients][0] -= drink[necessaryIngredients]
while True:
    choice = input("What would you like ?(espresso/latte/cappucino/report):").lower()
    if choice == 'report':
        for key in resources:
            print(f"{key} : {resources[key][0]}{resources[key][1]}")
    elif enoughResources(choice):
    # TO DO 4 : PROCESS COINS    
        print("Please insert coins.")
        pennies = coins["Penny"]*int(input("How many pennies?"))
        nickles = coins["Nickel"]*int(input("How many nickles?"))
        dimes = coins["Dime"]*int(input("How many dimes?"))
        quarters = coins["Quarter"]*int(input("How many quarters?"))
        total =pennies + nickles + dimes + quarters
        value=MENU[choice]["cost"]
    # TO DO 5 : IS THE TRASECTION POSSIBLE?
        if value > total:
            print(f"Not enough money to buy {choice}")
        else:
            change = total - value
            resources["money"][1]+= value
            print(f"Here is your change {change}")
            print(f"Enjoy Here is your {choice}")
            reduceIngredients (choice)
                 
     