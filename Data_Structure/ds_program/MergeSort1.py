# merge sorting for ascending order.
def merge_sort(list1):
    if len(list1) > 1:
        mid = len(list1)//2
        left_list = list1[:mid]
        right_list = list1[mid:]
        merge_sort(left_list)
        merge_sort(right_list)
        i = 0
        j = 0
        k = 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list1[k] = left_list[i]
                i = i + 1
                k = k + 1
            else:
                list1[k] = right_list[j]
                j = j + 1
                k = k + 1
        while i < len(left_list):
            list1[k] = left_list[i]
            i = i + 1
            k = k + 1
        while j < len(right_list):
            list1[k] = right_list[j]
            j = j + 1
            k = k + 1

num = int(input("Enter number of element:"))
list1 = [int(input("enter element:")) for x in range(num)]
print("Given list:",list1)
merge_sort(list1)
print("sorting in ascending order:",list1)

# merge sorting for descending order.
def merge_sort(list1):
    if len(list1) > 1:
        mid = len(list1)//2
        left_list = list1[:mid]
        right_list = list1[mid:]
        merge_sort(left_list)
        merge_sort(right_list)
        i = 0
        j = 0
        k = 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] > right_list[j]:
                list1[k] = left_list[i]
                i = i + 1
                k = k + 1
            else:
                list1[k] = right_list[j]
                j = j + 1
                k = k + 1
        while i < len(left_list):
            list1[k] = left_list[i]
            i = i + 1
            k = k + 1
        while j < len(right_list):
            list1[k] = right_list[j]
            j = j + 1
            k = k + 1

merge_sort(list1)
print("sorting in descending order:",list1)

# Algorithm:
# 1. Split the unsorted list.
# 2. Compare each of the elements and group them.
# 3. Repeat step 2 untill whole list is merged and sorted.