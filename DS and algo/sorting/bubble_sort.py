#Swapping the adjacent elements if they are in the wrong order
def bubble_sort(my_list):
    for i in range(len(my_list)-1,0,-1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list


list_to_sort = [4,2,6,5,1,3]
print(bubble_sort(list_to_sort))

print(bubble_sort([1]))
print(bubble_sort([1,0]))
print(bubble_sort([1,1,1,3,4,2]))
print(bubble_sort([1,-2,3,4,10,24,100,-300]))
