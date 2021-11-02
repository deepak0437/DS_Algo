num = int(input("enter length of list:"))
list1 = [int(input("Enter element:")) for i in range(num)]
print("Given list:",list1)
#sorting from ascending order without using min() function
for x in range(len(list1)):
    min_value = list1[x]
    for i in range(x+1,len(list1)):
        if list1[i] < min_value:
            min_value = list1[i]
    min_index = list1.index(min_value,x)
    list1[x] , list1[min_index] = list1[min_index] , list1[x]
print("Sorting list from ascending order:",list1)

#sorting from descending order without using max() function
for x in range(len(list1)):
    min_value = list1[x]
    for i in range(x+1,len(list1)):
        if list1[i] > min_value:
            min_value = list1[i]
    min_index = list1.index(min_value,x)
    list1[x] , list1[min_index] = list1[min_index] , list1[x]

print("Sorting list from descending order:",list1)


#sorting from ascending order without using min() and index value function
for x in range(len(list1)):
    min_index = x
    for i in range(x+1,len(list1)):
        if list1[i] < list1[min_index]:
            min_index = i
    list1[x] , list1[min_index] = list1[min_index] , list1[x]
print("Sorting list from ascending order:",list1)

