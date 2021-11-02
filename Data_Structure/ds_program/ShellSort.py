# shell sorting for ascending order.
def shell_sort(list1):
    gap = len(list1)//2
    while gap > 0:
        for index in range(gap,len(list1)):
            current_element = list1[index]
            pos = index
            while pos >= gap and current_element < list1[pos - gap]:
                list1[pos] = list1[pos - gap]
                pos = pos - gap
            list1[pos] = current_element
        gap = gap//2

list1 = [64,23,11,54,76,98,34,44]
print("Given list:",list1)
shell_sort(list1)
print("Sorting in ascending order:",list1)

# shell sorting for descending order.
def shell_sort(list1):
    gap = len(list1)//2
    while gap > 0:
        for index in range(gap,len(list1)):
            current_element = list1[index]
            pos = index
            while pos >= gap and current_element > list1[pos - gap]:
                list1[pos] = list1[pos - gap]
                pos = pos - gap
            list1[pos] = current_element
        gap = gap//2

shell_sort(list1)
print("Sorting in descending order:",list1)