# to get the coreect position of the pivot element.
# here we take pivot element as first element.
def pivot_place(list1,first,last):
    pivot = list1[first]
    left = first + 1
    right = last
    while True:
        while left <= right and list1[left] <= pivot:
            left = left + 1
        while left <= right and list1[right] >= pivot:
            right = right - 1
        if left > right:
            break
        else:
            list1[left] , list1[right] = list1[right] , list1[left]
    list1[first] , list1[right] = list1[right] , list1[first]
    return right

def quick_sort(list1,first,last):
    if first < last:
        p = pivot_place(list1,first,last)
        quick_sort(list1,first,p-1)
        quick_sort(list1,p+1,last)
# this is Quick sorting algroithm for ascending order.
list1 = [54,34,97,45,22,20,56,34]
print("Given list: ",list1)
n = len(list1)
quick_sort(list1,0,n-1)
print("Sorting in ascending order",list1)
#---------------------------------------------------
# here we take pivot element as first element.
def pivot_place(list1,first,last):
    pivot = list1[first]
    left = first + 1
    right = last
    while True:
        while left <= right and list1[left] >= pivot:
            left = left + 1
        while left <= right and list1[right] <= pivot:
            right = right - 1
        if left > right:
            break
        else:
            list1[left] , list1[right] = list1[right] , list1[left]
    list1[first] , list1[right] = list1[right] , list1[first]
    return right

def quick_sort(list1,first,last):
    if first < last:
        p = pivot_place(list1,first,last)
        quick_sort(list1,first,p-1)
        quick_sort(list1,p+1,last)

# this is Quick sorting algroithm for descending order.
list1 = [54,34,97,45,22,20,56,34]
n = len(list1)
quick_sort(list1,0,n-1)
print("Sorting in descending order",list1)

# Algorithm:
# 1. Select the pivot element.
# 2. Find out the correct position of pivot element in the
#    list by rearranging it.
# 3. Divide the list based on pivot element
# 4. sort the sublist recursively.