def linearsearch(list1,key):
    for x in range(len(list1)):
        if key == list1[x]:
            print(key,"Key element is found at index:",x)
            break
    else:
        print(key," is not found")

num = int(input("list length:"))
list1 = [int(input("Enter element:")) for i in range(num)]
print(list1)
key = int(input("Enter the key element:"))
linearsearch(list1,key)