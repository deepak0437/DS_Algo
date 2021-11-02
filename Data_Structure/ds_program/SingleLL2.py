#first create a class node.
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
#create empty linked list.
class LinkedList:
    def __init__(self):
        self.head = None
#add element at the beginning of the linked list.
    def add_begin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
#add element at the end of the linked list.
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
#add element after a node of the given linked list.
    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.next
        if n is None:
            print("Node is not present in given Linked List")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node
#add element before a node of the given linked list.
    def add_before(self,data,x):
        if self.head is None:
            print("Linked List is empty")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
        if n.next is None:
            print("Node is not found in given Linked List i.e",x)
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node
#print or travese all the element of the linked list.
    def printList(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,end=" ")
                n = n.next
#create an object and call class and function.
llist =LinkedList()
llist.add_begin(10)
llist.add_begin(20)
llist.add_begin(30)
llist.add_end(40)
llist.add_end(50)
llist.add_end(60)
llist.add_after(70,40)
llist.add_after(80,60)
llist.add_before(110,30)
llist.add_before(120,40)
llist.printList()
