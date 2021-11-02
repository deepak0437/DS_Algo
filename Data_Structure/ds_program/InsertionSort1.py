#insertion sorting for ascending order.
def insertionSort(my_list):
    for index in range(1,len(my_list)):
        current_element = my_list[index]
        pos = index
        while current_element < my_list[pos-1] and pos > 0:
            my_list[pos] = my_list[pos-1]
            pos = pos - 1
        my_list[pos] = current_element

list1= [97,43,54,12,34,23]
print("Given list:",list1)
insertionSort(list1)
print("Sorting list from ascending order:",list1)

#insertion sorting in desending order.8790
def insertionSort(my_list):
    for index in range(1,len(my_list)):
        current_element = my_list[index]
        pos = index
        while current_element > my_list[pos-1] and pos > 0:
            my_list[pos] = my_list[pos-1]
            pos = pos - 1
        my_list[pos] = current_element

list1= [97,43,54,12,34,23]
insertionSort(list1)
print("Sorting list from descending order:",list1)


#Algorithms:
# 1. Consider the first element to be sorted and the rest to be unsorted.
# 2. Take the first element in the unsorted part(u1) and compare it with
#     sorted part elements(s1).
# 3. if u1 < s1 then insert u1 in the correct index ,else leave it as it is.
# 4. Take next element in the unsorted part and compare with sorted elements.
# 5. Repeate 3 and 4 untill all the elements and sorted.
