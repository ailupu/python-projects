"""
Precondition:
You are given a list of houses grouped into neighborhoods.
The input is an array representing house numbers in each neighborhood. 
One sub-array represents one neighborhood. 

Task:
Reorganize the neighborhoods such that the houses in each neighborhood are in ascending order
No house numbers are repeated in a neighborhood. 
The neighborhood structure  must be preserved, meaning that the number of neighborhoods and the number of houses in each neighborhood should 
remain the same as given.

Example: 	h_list = [ [8, 2, 5], [1, 8, 4], [3, 6, 9] ]
Solution: 	new_list = [ [1, 2, 3], [4, 5, 8], [6, 8, 9] ]

"""

def sort_housing(h_list):
    nr = len(h_list[0])
    new_list = list()
    for el in h_list:
        for i in range(len(el)):
            new_list.append(el[i])
    
    print(new_list)
    new_list_sorted = sorted(new_list)
    print(new_list_sorted)
    
    if len(set(new_list_sorted)) != len(new_list_sorted):
        print(f'Duplicates! {new_list_sorted}')
        for i in range(len(new_list_sorted)-1):
            if new_list_sorted[i] == new_list_sorted[i+1]:
                flag = new_list_sorted[i-1]
                new_list_sorted[i-1] = new_list_sorted[i]
                new_list_sorted[i] = flag

    final_list = list()
    for el in range(0,len(new_list_sorted), nr):
        print(el)
        final_list.append(new_list_sorted[el:el+nr])
    print(final_list)
        


# def sort_housing(h_list):
#     new_list = list()
#     while len(h_list) == 3:
#         for i in range(len(h_list)):
#             flag = 0
#             new_list.append([])
#             min_el = h_list[i][0]
#             for j in range(len(h_list[i])):
#                 if h_list[i][j] < min_el:
#                     min_el = h_list[i][j]
#                     flag = j
#             new_list[i].append(min_el)
#             h_list[i].pop(flag)

#     print("h_list:", h_list)
#     print("new_list:", new_list)             

sort_housing([ [8, 2, 5], [1, 8, 4], [3, 6, 9] ])