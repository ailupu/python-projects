"""
Big O: categorize the algorithm time or memory based on your imput.

Example: If we have a string and we do a for to execute the lenght of the string, if the input grows 50% the algh grows with 50% 
        -> it's linear

Look for loopS! -> grows complexity

Important concepts:
    1. Growth is with respect to the input
    2. Constants are dropped
    3. Worst case is usually the way we measure

n log n algh: Quicksort
log n algh: Binary search trees    
"""

######## FROM UDEMY COURSE #########


"""
Time complexity - it is not measure in time (because sometimes the computer is fast)
                - it measures the operations that it takes to complete something

omega - the best case scenario
theta - average case
omicron (O) - worst case  (always!!)
"""

####### First BIG O -> O(n)########

#This runs in n operations - this is a straight line-> proportional
print("========  O(n)  ========")

def print_intems(n):
    for i in range(n):
        print(i)

print_intems(10)


print("========  Drop constants  ========")

#n + n = 2n but we drop constants => O(n)
def print_intems(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)

print_intems(10)


####### Second BIG O -> O(n^2)########
print("========  O(n^2)  ========")

#n*n => O(n^2) -> less eficient - loop between a loop
def print_intems(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

print_intems(10)


print("========  Drop non-dominants  ========")

def print_intems(n):
    for i in range(n):    #O(n^2)
        for j in range(n):
            print(i,j)
    for k in range(n):    #O(n)
        print(k)
                          #O(n^2+n) -> n is small so => O(n^2)

print_intems(10)


print("========  O(1)  ========")

# Constant time -> the numbver of operations remains constant 
# This is the most efficient big O
# Constant time

def add_item(n):
    return n + n


print("========  O(log n)  ========")
# It is very flat and efficient
# you have a list and you can divide by 2 everytime to find what you want
# Divide and Conquer

print("========  Different Terms for inputs  ========")

def print_intem(a,b):
    for i in range(a):   # This is O(a)
        print(i)

    for j in range(b):   # This is O(b)
        print(j)

                         # This is O(a + b)


print("========  Big O of Lists  ========")

my_list = [11, 3, 23, 7]

#This is O(1)
my_list.append(17)   # there is no indexing
my_list.pop() # takes out the last value - so no indexing

#This is O(n)
my_list.pop(0) # this index is wrong so the list needs to rearrange
my_list.insert(0,11) #this will reindex