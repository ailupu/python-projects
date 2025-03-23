"""
Given an array of integers representing an elevation map where the width of each bar is 1,
return how much rainwater can be trapped.
"""
# Step 1. Verify our constraints.
"""
1. Do the lefft and right sides of the graph count as walls? - No, the sides are not walls.
2. Will there be negative integers? - No all will be positives.
"""

# Step 2. Test cases.
"""
1. [0,1,0,2,1,0,3,1,0,1,2] -> 8
2. [] -> 0
3. [3] -> 0
4. [3,4,3] -> 0
"""

# Step 3. -> Come with a solution without code.
"""
current_water = min(maxL, maxR) - current_height
total += current_water
maxL = 0, maxR = 0
"""

# Step 4. Brute Force Coding
# Time O(n^2), Space O(1)
def trapping_rainwater(heights):
    total_water = 0
    for p in range(len(heights)):
        maxL = 0
        maxR = 0
        leftP = p
        rightP = p

        while leftP >= 0:
            maxL = max(maxL, heights[leftP])
            leftP -= 1
        
        while rightP < len(heights):
            maxR = max(maxR, heights[rightP])
            rightP += 1
        
        current_water = min(maxR, maxL) - heights[p]

        if current_water >= 0:
            total_water += current_water
   
    return total_water

print(trapping_rainwater([0,1,0,2,1,0,3,1,0,1,2]))
print(trapping_rainwater([]))
print(trapping_rainwater([3]))
print(trapping_rainwater([3,4,3]))

# Part 5. Optimal Solution
"""
1. Identify pointer with leser value.
2. Is this pointer value greater than or equal to max of that side. yes -> update the max on that side; no -> get water for that poiter + add to total
3. Move the pointer inwords.
4. Repeat for the other pointer.
"""
# Time O(N), Space: O(1)
def optimal_trapping_rainwater(heights):
    left = 0
    right = len(heights) -1
    left_max = 0
    right_max = 0
    total_water = 0

    while left < right:
        if heights[left] <= heights[right]:
            if heights[left] >= left_max:
                left_max = heights[left]
            else:
                total_water += left_max - heights[left]
            left += 1
        else:
            if heights[right] >= right_max:
                right_max = heights[right]
            else:
                total_water += right_max - heights[right]
            right -= 1
    return total_water
            
print(optimal_trapping_rainwater([0,1,0,2,1,0,3,1,0,1,2]))
print(optimal_trapping_rainwater([]))
print(optimal_trapping_rainwater([3]))
print(optimal_trapping_rainwater([3,4,3]))