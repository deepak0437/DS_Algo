def linearsearch(list1,key):
    list2 = []
    num = False
    for x in range(len(list1)):
        if key == list1[x]:
            num = True
            list2.append(x)
    if num == True:
        print(key,"Key element is found at index:")
        for x in list2:
            print(x)
    else:
        print(key,"Key is not found")
#linear_search for duplicate value
#if duplicate values are present in list
list1 = [12,98,54,66,44,88,56,44,77,33,20,44]
print(list1)
key = int(input("Enter the key element:"))
linearsearch(list1,key)
# DEBUG:
