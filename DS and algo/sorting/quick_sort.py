#Start with a list
# Take the first value (i) and verify if the next number is greater than or lower than
# Change the first lower than variable with the first grater than value
# Change the second lower with the second grater and so on
# When that is done swap the first element with the last element that was lower than this
# Run QS again on the left and right of the first element that is now swapped (i)
# Make this recursion afetr every cut in half


##########  PIVOT(helper funtion for QS) ###########
def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index+1,end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list,swap_index,i)

    swap(my_list, pivot_index, swap_index)

    return swap_index

my_list = [4,6,1,7,3,2,5]
print(pivot(my_list,0,6))
print(my_list)

############## QUICK SORT ###############

def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index-1)
        quick_sort_helper(my_list, pivot_index+1, right)

    return my_list

def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list)-1)

print(quick_sort(my_list))


######## QS BIG O #######
#Pivot - O(n)
# Recursive - O(log n)
#QS is O(n log n) - best case and average case

# Worst case is when we have sorted aria
# The pivot will run until it finds something that is wrong
# O(n^2)

#Qs is good when you know you have lots of variables out fo order

