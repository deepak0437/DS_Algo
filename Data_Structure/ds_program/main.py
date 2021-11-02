class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add_begin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.next
        if n is None:
            print("Node is not present in linked list i.e",x)
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node
    def add_before(self,data,x):
        if self.head is None:
            print("Linked list is empty!")
            return
        if self.head.data == x:
            new_node =Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
        if n.next is None:
            print("Node is not present in linkedlist i.e",x)
        else:
            new_node = Node(data)
            new_node.next = n.next
            self.head = new_node
    def remove_begin(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            self.head = self.head.next
    def remove_end(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            n = self.head
            while n.next.next is not None:
                n = n.next
            n.next = None
    def count_node(self):
        n = self.head
        count = 0
        while n is not None:
            count = count + 1
            n = n.next
        print("Total number of nodes present in linkedlist:",count)
    def printList(self):
        if self.head is None:
            print("Linkedlist is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data,end=" ")
                n = n.next
llist = LinkedList()
llist.add_begin(20)
llist.add_begin(10)
llist.add_end(30)
llist.add_end(40)
llist.add_after(50,10)
llist.add_after(60,30)
llist.remove_begin()
llist.remove_end()
llist.count_node()
llist.printList()  
