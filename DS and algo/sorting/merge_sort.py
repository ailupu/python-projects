#2 sorted list it is easy to combine them in a new sorted list.
#You have a big list and you break it in half until you have lists with only one intem in it.
# take 2 of the items that are sorted until you have them all grouped in 2
# and than take 2 of the lists and sort them and you will have 2 lists of 4 items and so on...


########## MERGE (when 2 lists are sorted) #############
def merge1(list1, list2):
    combined = []
    lenght = len(list1)+len(list2)
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] < list2[j] and list1[i] not in combined:
                combined.append(list1[i])
            elif list1[i] > list2[j] and list2[j] not in combined:
                combined.append(list2[j])

    if list1[-1] > list2[-1]:
        for i in range(len(list1)):
            if list1[i] not in combined:
                combined.append(list1[i])
    else:
        for i in range(len(list2)):
            if list2[i] not in combined:
                combined.append(list2[i])
        
    return combined

list1 = [1,3,7,8]
list2 = [2,4,5,6]
print(merge1(list1,list2))

#Another way to do it!

def merge2(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined

print(merge2([1,2,7,8], [3,4,5,6]))


############ MERGE SORT #############

#1) break lists in half
#2) base case: when len(the_list) is 1
#3) use merge() to put lists together

def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid_index = int(len(my_list)/2)
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])

    return merge2(left,right)

print(merge_sort([3,1,4,2]))

#### BIG O - merge sort ####
# Space complexity: 1 list -> left list, right list -> and so on until you have 1 => O(n)
# Time comeplexity: O(logn) + while O(n) -> O(nlogn)