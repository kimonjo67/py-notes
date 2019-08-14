'''
Samuel Mwangi
Lab 9

'''

## Function that accepts two values and returns the sum
def sumFunction(x,y):
    return x + y

num1 = int(input("Enter integer: "))
num2 = int(input("Enter integer: "))

print(sumFunction(num1,num2))


## Function that accepts 3 numbers and returns the maximum
def maxValue(x,y,z):
    if x > y and x > z:
        print("max number is" , x)
    elif y > x and y > z:
        print("max number is", y)
    elif z > x and z > y:
        print("max number is", z)

num1 = int(input("Enter integer: "))
num2 = int(input("Enter integer: "))
num3 = int(input("Enter integer: "))

maxValue(num1, num2, num3)


## Function that accepts a number and string, print out string as many times as the number
def stringPrint():
    stringValue = input("Enter a string: ")
    number1 = int(input("Enter number: "))
    print(stringValue * number1)

stringPrint()
    
## Function that prints in increasing order
list1 = []
def increasingOrder():
    end = "n"
    while end != "y":        
        number1 = int(input("Enter integers: "))
        list1.append(number1)       
        end = input("End game, y or n: ")
        print(list1)
    print(sorted(list1))

increasingOrder()




