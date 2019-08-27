'''
This program reads numbers from user and stores the prime in one list and the non primes
 in another list.

'''
# create 2 empty lists prime and non-prime
# read user input numbers
# create loop with sentinal value of -1
# compute if number is prime
# if prime, append it to primeList and vice versa
# No duplicates on list

# priuserNumt lists
primeList = []
nonPrimeList = []

print("Check if number are Prime or Not")
print("To close, type -1")

def prime():    
    num = int(input("please enter a number: "))
    ## PRIME NUMBERS
    end = 0
    while end != -1:
        if num > 1:
            # loop through the number in the set
            for num in range(2,num):
                #loop through check number if divisible
                for x in range(2,num):
                    if (num % x ) == 0:
                        print(num, "NOT a prime", x , "*", num//x , " = ", num )
                        break
                else:
                    print(num, "is a PRIME number")
        else:
            print(num, "NOT a prime")

        end = int(input("Enter -1 to end or 0 to continue: "))
        if end == 0:
            return prime()

prime()
