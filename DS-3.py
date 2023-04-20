class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None

    # insert a node in to BST
    def insert(self,data):
        if self.key == None:
            self.key = data
            return f'item {data} added to empty Tree'
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
                
            else:
                self.lchild = BST(data)
                return f'item {data} added to left sub-tree'
        else:
            if self.rchild:
                self.rchild.insert(data)
                
            else:
                self.rchild = BST(data)
                return f'item {data} added to right sub-tree'

    # search whether a node is present in BST        
    def search(self,data):
        if self.key == data:
            print(f'item {data}  found in tree')
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print(f'item {data} not found in tree')
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print(f'item {data} not found in tree')

    # preorder traversal in BST
    def preOrder(self):
        print(self.key,end='--->')
        if self.lchild:
            self.lchild.preOrder()
        if self.rchild:
            self.rchild.preOrder()

    # inorder traversal in BST
    def inOrder(self):
        if self.lchild:
            self.lchild.inOrder()
        print(self.key,end='--->')
        if self.rchild:
            self.rchild.inOrder()
    
    # postorder traversal in BST
    def postOrder(self):
        if self.lchild:
            self.lchild.postOrder()
        if self.rchild:
            self.rchild.postOrder()
        print(self.key,end='--->')

    # delete node in BST
    def delete(self,data):
        if self.key is None:
            print('BST is empty')
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                print(f'Given node {data} not found in BST')

        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print(f'Given node {data} not found in BST')
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = self.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key)
        return self



    
               


root = BST(None)
print(root.key)
list1 = [10,5,15,3,20]
for i in list1:
    root.insert(i)

print(root.key)
print(root.lchild)
print(root.rchild)
root.search(10)

print('pre-order traversal')
root.preOrder()
print()
print('in-order traversal')
root.inOrder()
print()
print('post-order traversal')
root.postOrder()
print()
print('delete')
root.delete(10)
root.preOrder()

