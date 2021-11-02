list1 = []
num = int(input("Enetr length of list:"))
print("Enter list:")
for k in range(num):
    list1.append(int(input()))
# sorting in ascending order.
print("Given list:",list1)
for i in range(len(list1)-1):
    for x in range(len(list1)-1-i):
        if list1[x] > list1[x+1]:
            list1[x] , list1[x+1] = list1[x+1] , list1[x]
            print(list1)
        else:
            print(list1)
    print("------------------------")
print("Sorting list from ascending order:",list1)
print("================================")

#sorting in descending order.
for i in range(len(list1)-1):
    for x in range(len(list1)-1-i):
        if list1[x] < list1[x+1]:
            list1[x] , list1[x+1] = list1[x+1] , list1[x]
            print(list1)
        else:
            print(list1)
    print("------------------------")
print("Sorting list from descending order:",list1)


#Algorithm:
# 1. Starting with the first element (index = 0), compare the current element 
# with the next element of the list.
# 2. if the current element is greater than the next element of the list the
# swap them.
# 3. If the current element is less than thenext element, move to the next element
# and repeat the step 1.