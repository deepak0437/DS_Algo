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
            print("Double Linked List is not empty!")
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
            print("double LinkedList is empty! so we can't add element")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.next
            if n is None:
                print("Given node is present in Linked List i.e",x)
            else:
                new_node = Node(data)
                new_node.next = n.next
                new_node.prev = n
                if n.next is not None:
                    n.next.prev = new_node
                n.next = new_node
    def add_before(self,data,x):
        if self.head is None:
            print("Double Linked List is empty! so we can't add element.")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.next
            if n is None:
                print("Given node is not present in LinkedList i.e",x)
            else:
                new_node = Node(data)
                new_node.next = n
                new_node.prev = n.prev
                if n.prev is not None:
                    n.prev.next = new_node
                else:
                    self.head = new_node
                n.prev = new_node
    def remove_begin(self):
        if self.head is None:
            print("Doubl Linked list is empty! so we can't delete any node.")
            return
        if self.head.next is None:
            self.head = None
            print("Linked List is empty after deleting the node.")
        else:
            self.head = self.head.next
            self.head.prev = None
    def remove_end(self):
        if self.head is None:
            print("Double Linked list is empty! so we can't delete any node")
            return
        if self.head.next is None:
            self.head = None
            print("Linked List is empty after deleting the node.")
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.prev.next = None
    def remove_byvalue(self,x):
        if self.head is None:
            print("Double Linked list is empty!so we can't delete any node.")
            return
        if self.head.next is None:
            if x == self.head.data:
                self.head = None
            else:
                print("given Node is not present in linked ist")
            return
        if self.head.data == x:
            self.head = self.head.next
            self.head.prev = None
            return
        n = self.head
        while n.next is not None:
            if x == n.data:
                break
            n = n.next
        if n.next is not None:
            n.next.prev = n.prev
            n.prev.next = n.next
        else:
            if n.data == x:
                n.prev.next = None
            else:
                print("Given node is not present in linked list.")        
    def count_nodes(self):
        n = self.head
        count = 0
        while n is not None:
            count = count + 1
            n = n.next
        print("total number of node present in linkedlist is:",count)
    def printlist(self):
        if self.head is None:
            print("Double LinkedList is Empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data,end=" ")
                n = n.next
llist = DoubleLinkedList()
llist.add_begin(20)
llist.add_begin(10)
llist.add_end(30)
llist.add_end(40)
llist.add_after(50,40)
llist.add_after(80,50)
llist.add_before(60,80)
llist.add_before(70,80)
llist.remove_begin()
llist.remove_end()
llist.remove_byvalue(40)
llist.count_nodes()
llist.printlist()
