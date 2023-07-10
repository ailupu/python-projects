#Function that calls itself...until it doesn't

def funcThree():
    print("Three")

def funcTwo():
    funcThree()
    print("Two")

def funcOne():
    funcTwo()
    print("One")

funcOne()

#example: factorial -> 4 * 3 *2 *1 -> 4!

def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)
print(factorial(4))