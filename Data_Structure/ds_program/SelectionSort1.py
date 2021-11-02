list1 = [45,76,32,54,98,12,22,32]
print("Given list:",list1)
#selection sorting from an ascending order.
for x in range(len(list1)-1):
    min_value = min(list1[x:])
# Here x is used for printing duplicate value from list.
    min_index = list1.index(min_value,x)
    list1[x] , list1[min_index] = list1[min_index] , list1[x]
print("Sorting list from ascending order:",list1)

#selection sorting from an descending order.
for x in range(len(list1) -1):
    min_value = max(list1[x:])
    min_index = list1.index(min_value,x)
    list1[x] , list1[min_index] = list1[min_index] , list1[x]
print("Sorting list from descending order:",list1)

#algorithm of selection sorting:
# 1.First find out the minimum or maximum value.
# 2.Then swap minimum or maximum value to 0th positon or index.
# 3.Take a sublist (except sorted part) and repeat step 1 and 2.
