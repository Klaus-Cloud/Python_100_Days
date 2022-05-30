print("Welcome to the tip calculator\n")
bill=float(input("What was the total bill?\n"))
numberPeople=int(input("How many people to split the bill?\n"))
percentageTip =int(input("What percentage tip 3ould you like to give?\n"))
tip=bill*percentageTip*0.01/numberPeople
final_tip= round(tip,4)
answer=f"Each person should pay: $ {final_tip}"
print(answer)