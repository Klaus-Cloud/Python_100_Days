# def add(*args):
#     solution = 0
#     for n in args:
#         solution += n
#     print(solution)
# add(1, 2, 3, 4, 5)

def calculate(**kwargs):
    # for key,value in kwargs.items():
    #     print(value)
    num = 0
    num += kwargs["num1"]
    num *= kwargs["num2"]
    print(num)

calculate(num1=10, num2 =11)


