class Node:
    __slots__ = '_element' , '_left' , '_right'
    def __init__(self,element,left=None,right=None):
        self._element = element
        self._left = left
        self._right = right

class BinaryTree:
    def __init__(self):
        self._root = None
    def maketree(self,e,left,right):
        self._root = Node(e,left._root,right._root)
    def inorder(self,troot):
        if troot is not None:
            self.inorder(troot._left)
            print(troot._element,end=" ")
            self.inorder(troot._right)

p = BinaryTree()           
q = BinaryTree()
r = BinaryTree()
s = BinaryTree()
t = BinaryTree()
u = BinaryTree()
v = BinaryTree()
a = BinaryTree()
p.maketree(40,a,a)
q.maketree(20,a,a)
r.maketree(30,q,p)
s.maketree(70,a,a)
t.maketree(90,a,a)
u.maketree(80,s,t)
v.maketree(60,r,u)
v.inorder(v._root)
