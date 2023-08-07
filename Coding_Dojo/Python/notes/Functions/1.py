#  Function

def another_func(multiplier):
    print("howdy " *multiplier)

another_func(5)


def birthday_funk(month="june"):
    if month == "august":
        print("happy Birthday")
    else:
        print("hi")

birthday_funk()


def num(num1, num2):
    return(num1 + num2)

print(num(2,7))