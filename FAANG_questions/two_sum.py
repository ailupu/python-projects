"""
Given an array of integers, return the indices of the two numbers that add up to a given target.
- [1,3,7,9,2]
- target = 11
Return an array with the indices.
"""

# 1. Verify the constraints.
# Are all the numbers positive or can there be negatives? - All numbers are positive
# Are there duplicates numbers in the array? - No
# Will there always be a solution available? - No there may not be always a solution.
# What do we return if there is no solution. - Just return null.
# Can there be multiple pairs? - No only 1 pair.

# 2. Write out some test cases.
"""
1. [1,3,7,9,2] t = 11 => [3,4]
2. [1,3,7,9,2] t = 25 => null
3. [] t = 1 => null
4. [5] t = 5 => null
5. [1,6] t = 7 => [0,1]
"""

# 3. Figure out a solution without code.
"""
Come up with a working solution.
[1,3,7,9,2] t = 11 -> try every possible solution.
You start with first number and add with the rest of numbers. Do that until you find the good match. -> 2 pointer technique
number_to_find = target - nums[P1] - P1 will be first 1 then 3 etc. 
number_to_find is P2 -> wil be 3, 7, 9 etc
When you move P1 at 3 you reset the P2 at 7. An move form there.
"""

# 4. Write out out solution in code.
def two_sum(nr_list, target):
    for i in range(len(nr_list)):
        p1 = nr_list[i]
        p2 = target - p1
        for j in range(i+1,len(nr_list)):
            if nr_list[j] == p2:
                return [i,j]
    return None

# print(two_sum([1,3,7,9,2], 11))
# print(two_sum([1,3,7,9,2], 25))
# print(two_sum([], 25))
# print(two_sum([1], 25))
# print(two_sum([1,6], 7))

# Time complexity - if the nums array gets bigger how much time it will take.
# first for loop - time complexity of N
# second for loop - time complexity of N
# This code will wun O(N^2)

# Optimizing our solution
# use a hashmap : [number_to_find : index]
def two_sum(nums, target):
    nums_map = {}
    for i,num in enumerate(nums):
        complement = target - num
        if complement in nums_map:
            return [nums_map[complement], i]
        nums_map[num] = i
    return None

print(two_sum([1,3,7,9,2], 11))
print(two_sum([1,3,7,9,2], 25))
print(two_sum([], 25))
print(two_sum([1], 25))
print(two_sum([1,6], 7))
