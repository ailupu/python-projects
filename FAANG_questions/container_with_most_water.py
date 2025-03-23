"""
You are given an array of positives integers where each integer represents the height
of a vertical line on a chart.
Find 2 lines which together with the x-axis forms a container that would hold 
the greatest amount of water. 
Return the area of water it would hold.

[1,8,6,2,9,4] => length = 8 -> width = 3 (index of 9 - index of 8)
area = lenght X width
"""

"""
Questions:
1. Does the thickness of the lines affet the area? No, assume they take up no space.
2. Do the left and right sides of the graph count as walls? - No the sides cannot be used to form a container.
3. Does a higer line inside our container affect out area? - Lines inside teh container don't affect the area.
"""

"""
Write the test cases:
[7,1,2,3,9] -> 7 and 9 = 28
[] -> 0
[7] -> 0
[6,9,3,4,5,8] -> 6x5=30; 8x4=32
"""

"""
Figure out a solution without code.
area = l x w -> min(a,b) x (index_b - index_a)
initialize maxArea = 0
"""

def container_with_max_water(vertical_lines):
    max_area = 0
    for i in range(len(vertical_lines)):
        for j in range(i+1,len(vertical_lines)):
            calculated_area = min(vertical_lines[i], vertical_lines[j]) * (j-i)
            if calculated_area > max_area:
                max_area = calculated_area
    return max_area

print(container_with_max_water([6,9,3,4,5,8]))
print(container_with_max_water([]))


# Optimize solution
"""
Shifting point.
"""
def optimal_container_with_max_water(vertical_lines):
    p1 = 0
    p2 = len(vertical_lines) -1
    max_area = 0
    while p1 < p2:
        height = min(vertical_lines[p1],vertical_lines[p2])
        width = p2 - p1
        area = height * width
        max_area = max(max_area, area)
        if vertical_lines[p1] <= vertical_lines[p2]:
            p1 += 1
        else:
            p2 -= 1
    return max_area

print(optimal_container_with_max_water([6,9,3,4,5,8]))
print(optimal_container_with_max_water([]))