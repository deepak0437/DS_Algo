class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class DoubleLinkedList:
    def __init__(self):
        self.head = None
    def add_emptylist(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Doubly Linked List is not empty!")
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
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
            new_node.prev = n
    def add_after(self,data,x):
        if self.head is None:
            print("Linkedlist is empty, we can insert any element!")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.next
        if n is None:
            print("given node is not present in given linkedlist i.e",x)
        else:
            new_node = Node(data)
            new_node.next = n.next
            new_node.prev = n
            if n.next is not None:
                n.next.prev = new_node
            n.next = new_node
    def add_before(self,data,x):
        if self.head is None:
            print("Linkedlist is empty, we can insert any element!")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.next
        if n is None:
            print("given node is not present in given linkedlist i.e",x)
        else:
            new_node = Node(data)
            new_node.next = n
            new_node.prev = n.prev
            if n.prev is not None:
                n.prev.next = new_node
            else:
                self.head = new_node
            n.prev = new_node
    def count_nodes(self):
        n = self.head
        count = 0
        while n is not None:
            count = count + 1
            n = n.next
        print("total number of node present in linkedlist is:",count)
    def printlistforward(self):
        if self.head is None:
            print("Double Linked List is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data,end=" ")
                n = n.next
    def printlistbackward(self):
        if self.head is None:
            print("Double Linked List is empty!")
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            while n is not None:
                print(n.data,end=" ")
                n = n.prev
llist = DoubleLinkedList()
llist.add_begin(20)
llist.add_begin(10)
llist.add_end(30)
llist.add_end(40)
llist.add_after(50,30)
llist.add_before(60,50)
llist.count_nodes()
llist.printlistforward()
