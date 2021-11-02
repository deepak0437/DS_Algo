def binarysearch(list1,key):
    low = 0
    high = len(list1) - 1
    found = False
    while low <= high and not found:
        mid = (low + high) // 2
        if key == list1[mid]:
            found = True
        elif key > list1[mid]: 
            low = mid + 1
        else:
            high = mid - 1
    if found == True:
        print(key, "key element is found at index:",mid)
    else:
        print(key,"key element is not found" )

list1 = [23,43,66,76,55,33,98,54]
list1.sort()
print(list1)
key = int(input("Enter the key element:"))
result = binarysearch(list1,key)

