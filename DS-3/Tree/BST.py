class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    # pre-order traversal
    def preOrder(self):
        if self.key is None:
            print('cant pre-order traverse')
            return
        else:
            print(self.key,'---->',end='')
            if self.lchild:
                self.lchild.preOrder()
            if self.rchild:
                self.rchild.preOrder()
    
    # in-order traversal
    def inOrder(self):
        if self.key is None:
            print('cant in-order traverse')
            return
        else:
            if self.lchild:
                self.lchild.inOrder()
            print(self.key,'---->',end='')
            if self.rchild:
                self.rchild.inOrder()

    # post-order traversal
    def postOrder(self):
        if self.key is None:
            print('cant post-order travers')
        else:
            if self.lchild:
                self.lchild.postOrder()
            if self.rchild:
                self.rchild.postOrder()
            print(self.key,'---->',end='')


    # insertion of node 
    def Insertion(self,data):
        if self.key is None:
            self.key = data
            print(f'item {data} at empty BST')
            return
        elif self.key == data:
            return
        else:
            if data < self.key:
                if self.lchild:
                    self.lchild.Insertion(data)
                else:
                    self.lchild = BST(data)
                    print(f'item {data} is added at left sub-tree')
            else:
                if self.rchild:
                    self.rchild.Insertion(data)
                else:
                    self.rchild = BST(data)
                    print(f'item {data} is added at right sub-tree')

    # searching node
    def Searching(self,data):
        if self.key is None:
            print('BSt is empty,so cant find search')
            return
        elif self.key == data:
            print(f'item {data} is found in BST')
            return
        else:
            if data < self.key:
                if self.lchild:
                    self.lchild.Searching(data)
                else:
                    print(f'item {data} is not found in BST')
            else:
                if self.rchild:
                    self.rchild.Searching(data)
                else:
                    print(f'item {data} is not found in BST')

    # deleting node
    def delete(self,data,curr):
        if self.key is None:
            print('cant delete,bst is empty')
        elif data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data,curr)
            else:
                print(f'no such items {data}in this BST')
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data,curr)
            else:
                print(f'no such items {data}in this BST')
        else:
            if self.lchild is None:
                temp = self.rchild
                if curr == data:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild  = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                if curr == data:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = self.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key,curr)

        return self
    
    # get minimum
    def get_minimum(self):
        if self.key is None:
            print('cant get minimum ,because its empty')
            return
        elif self.key is not None and self.lchild is None:
            print(f'minimum value is:',self.key)
            return
        else:
            self.lchild.get_minimum()
    
    # get maximum
    def get_maximum(self):
        if self.key is None:
            print('cant get maximum ,because its empty')
            return
        elif self.key is not None and self.rchild is None:
            print(f'maximum value is:',self.key)
            return
        else:
            self.rchild.get_maximum()


          
def count(node):
    if node is None:
        return 0
    else:
        return 1+count(node.lchild)+count(node.rchild)
        
list = [2,5,7,8,0]
bst = BST(5)
bst.Insertion(6)
bst.Insertion(4)
bst.Insertion(9)
for i in list:
    bst.Insertion(i)
bst.Searching(6)
if count(bst) > 1:
  bst.delete(5,bst.key)
else:
    print('cant delete root node')
bst.preOrder()
print()
bst.inOrder()
print()
bst.postOrder()
print()
bst.get_minimum()
bst.get_maximum()


# insertion
# O(logn) T / worst O(n)
# O(1) S
# searching
# O(logn) T/ worst O(n)
# O(1) S
# deletion
# O(logn) T / worst O(n)
# O(1) S
# traversing
# O(n) T
# O(1) S
# getmin
# O(logn) / best O(1) T
# O(1) S
# get max   
# # O(logn) / best O(1) T
# O(1) S     