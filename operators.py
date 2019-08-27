
def operation(number1, number2, stringV):
    print("press 1 for +, 2 for - and 3 for * ")

    operation = int(input("Enter operation number between 1, 2 and 3: "))
    if operation == 1:
        print(number1 + number2)
        print(number1 * stringV)
    elif operation == 2:
        print(number1 - number2)
    else:
        print(number1 * number2)

number1 = int(input("Please enter number: "))
number2 = int(input("Please enter number: "))
stringV = "Hello"

operation(number1, number2, stringV)