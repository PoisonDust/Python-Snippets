while True:
    equation = input("Please enter a operator: ")
    first = input("Please enter your first number: ")
    second = input("Please enter your second number: ")
    if equation == "+":
        print("Your answer is:", int(first) + int(second))
    elif equation == "-":
        print("Your answer is:", int(first) - int(second))
    elif equation == "*":
        print("Your answer is:", int(first) * int(second))
    elif equation == "/":
        print("Your answer is:", int(first) / int(second))
    else:
        print("")
        print("Your equation could not be finished due to an invalid operator.")
        print("")
        print("Available Operators:")
        print("+")
        print("*")
        print("-")
        print("/")
        print("")
        print("Your entered operator:", equation)
