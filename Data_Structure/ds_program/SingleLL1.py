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
            print("node is not present in given list i.e",x)
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node
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
            print("Node is not present in given Linkedlist i.e",x)
        else:
            new_node = Node(data)
            new_node.next = n.next
            self.head = new_node
    def remove_begin(self):
        if self.head is None:
            print("Linked List is empty!")
        else:
            self.head = self.head.next
    def remove_end(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n.next.next is not None:
                n = n.next
            n.next = None
    def remove_value(self,x):
        if self.head is None:
            print("Linked List is empty!")
            return
        if x == self.head.data:
            self.head = self.head.next
            return
        n = self.head
        while n.next is not None:
            if x == n.next.data:
                break
            n = n.next
        if n.next is None:
            print("Node is not present in given linkedlist i.e",x)
        else:
            n.next = n.next.next
    def count_nodes(self):
        n = self.head
        count = 0
        while n is not None:
            count = count + 1
            n = n.next
        print("total number of node present in linkedlist is:",count)
    def reverse_node(self):
        prev = None
        n = self.head
        while n is not None:
            next = n.next
            n.next = prev
            prev = n
            n = next
        self.head = prev
    def printList(self):
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data,end=" ")
                n = n.next

llist = LinkedList()
llist.add_begin(10)
llist.add_begin(20)
llist.add_end(30)
llist.add_end(50)
llist.add_after(40,30)
llist.add_after(60,20)
llist.add_before(90,20)
llist.remove_begin()
llist.remove_end()
llist.remove_value(10)
llist.count_nodes()
llist.reverse_node()
llist.printList()
