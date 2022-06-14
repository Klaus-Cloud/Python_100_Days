# The exceptions: The try catch except finally Pattern
# try:
#     with open('a_file.txt') as file:
#         file.read()
#     cool_list = [0, 1, 2]
#     print(cool_list[3])
# except FileNotFoundError:
#     with open('a_file.txt', "w") as file:
#         file.write("Hello")
# except IndexError as error_message:
#     print(f"IndexError: {error_message}")
# else:
#     with open('a_file.txt') as file:
#         content = file.read()
#         print(content)
#
# finally:
#     raise KeyError("This is an error that I made up")

score = int(input("Score: "))
if score > 10:
    raise ValueError("The score cannot exceed 10 points!")
gpa = float(input("Average: "))
number_Tests = int(input("Number of tests: "))

new_gpa = (gpa + score*number_Tests) / (number_Tests + 1)

print(gpa)

