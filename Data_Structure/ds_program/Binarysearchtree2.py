#we delete an element from binary search tree
class Node:
    __slots__ = '_element' , '_left' , '_right'
    def __init__(self,element,left=None,right=None):
        self._element = element
        self._left = left
        self._right = right
class BinarysearchTree:
    def __init__(self):
        self.root = None
    def insert(self,troot,e):
        temp = None
        while troot is not None:
            temp = troot
            if e ==  troot._element:
                return
            elif e < troot._element:
                troot = troot._left
            elif e > troot._element:
                troot = troot._right
        n = Node(e)
        if self.root is not None:
            if e < temp._element:
                temp._left = n
            else:
                temp._right = n
        else:
            self.root = n

    def inorder(self,troot):
        if troot is not None:
            self.inorder(troot._left)
            print(troot._element,end=" ")
            self.inorder(troot._right)
           
B = BinarysearchTree()
B.insert(B.root,20)
B.insert(B.root,10)
B.insert(B.root,40)
B.insert(B.root,60)
B.insert(B.root,50) 
B.insert(B.root,80)
B.insert(B.root,90)
B.inorder(B.root)