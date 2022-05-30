from functions import operations
def calculator():
    num1 = float(input("Insert number 1:\n"))

    for key in operations:
        print(key)
    gameOver =False
    while not gameOver:
        symbol = input("Which operation would to like to use?\n")
        num2 = float(input("Insert number 2:\n"))
        chosen_operation =operations[symbol]
        answer=chosen_operation(num1,num2)
        print(f"{num1} {symbol} {num2} = {answer}")
        num1=answer
        choice = input(f"Type 'y' to continue calculationg with {answer}, otherwise type 'n' to insert a new value or e to exit  :").lower()
        if choice == "e":
            gameOver=True
        elif choice =="n" :
            calculator()
calculator()



