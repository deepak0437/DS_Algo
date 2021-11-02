# to get the coreect position of the pivot element.
# here we take pivot element as last element.
def pivot_place(list1,first,last):
    pivot = list1[last]
    left = first
    right = last - 1
    while True:
        while left <= right and list1[left] <= pivot:
            left = left + 1
        while left <= right and list1[right] >= pivot:
            right = right - 1
        if left > right:
            break
        else:
            list1[left] , list1[right] = list1[right] , list1[left]
    list1[last] , list1[left] = list1[left] , list1[last]
    return left

def quick_sort(list1,first,last):
    if first < last:
        p = pivot_place(list1,first,last)
        quick_sort(list1,first,p-1)
        quick_sort(list1,p+1,last)
# this is Quick sorting algroithm for ascending order.
list1 = [76,44,22,98,33,12,66,44,37]
print("Given list:",list1)
n = len(list1)
quick_sort(list1,0,n-1)
print("Sorting in ascending order",list1)

#---------------------------------------------------
# to get the coreect position of the pivot element.
# here we take pivot element as last element.
def pivot_place(list1,first,last):
    pivot = list1[last]
    left = first
    right = last - 1
    while True:
        while left <= right and list1[left] >= pivot:
            left = left + 1
        while left <= right and list1[right] <= pivot:
            right = right - 1
        if left > right:
            break
        else:
            list1[left] , list1[right] = list1[right] , list1[left]
    list1[last] , list1[left] = list1[left] , list1[last]
    return left

def quick_sort(list1,first,last):
    if first < last:
        p = pivot_place(list1,first,last)
        quick_sort(list1,first,p-1)
        quick_sort(list1,p+1,last)
# this is Quick sorting algroithm for descending order.
list1 = [76,44,22,98,33,12,66,44,37]
n = len(list1)
quick_sort(list1,0,n-1)
print("Sorting in descending order",list1)