################# BST ##############################
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
    def delete(self,data,curr):
        if self.key is None:
            print('BST is empty')
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data,curr)
            else:
                print(f'Given node {data} not found in BST')

        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data,curr)
            else:
                print(f'Given node {data} not found in BST')
        else:
            if self.lchild is None:
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = self.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key,curr)
        return self
    
    # to find minimum node in the given BST
    def min_node(self):
        current = self
        while current.lchild:
            current = current.lchild
        print('node with smallest key is:',current.key)

    # to find maximum node in the given BST
    def max_node(self):
        current = self
        while current.rchild:
            current = current.rchild
        print('node with largest key is:',current.key)



    
def count(node):
    if node is None:
        return 0
    return 1+count(node.lchild)+count(node.rchild)               


root = BST(10)
list1 = [1,2,100]
for i in list1:
    root.insert(i)
print(root.key)
print(count(root))
if count(root)>1:
    root.delete(10,root.key)
else:
    print('cant perform deletion operation')

print('pre-order')
root.preOrder()
print()
root.min_node()
print()
root.max_node()


# print(root.key)
# print(root.lchild)
# print(root.rchild)
# root.search(10)

# print('pre-order traversal')
# root.preOrder()
# print()
# print('in-order traversal')
# root.inOrder()
# print()
# print('post-order traversal')
# root.postOrder()
# print()
# print('delete')
# root.delete(10)
# root.preOrder()

#################### END BST ##########################


########################### HEAP ##########################

# ----------- BINARY HEAP ------------------#

# implementation using heapq module

import heapq
heap = []
heapq.heappush(heap,10)
print(heap)
heapq.heappush(heap,1)
print(heap)
heapq.heappush(heap,5)
print(heap)
heapq.heappop(heap)
print(heap)
heapq.heappop(heap)
print(heap)
heapq.heappop(heap)
print(heap)
list1 = [1,3,5,2,4,6]
heapq.heapify(list1)
print(list1)
print(heapq.heappushpop(list1,89))
print(list1)
print(heapq.heapreplace(list1,100))
print(list1)

print(heapq.nsmallest(2,list1))
print(heapq.nlargest(3,list1))

list = [(1,'ashu'),(2,'ann'),(3,'konn')]
heapq.heapify(list)
print(list)
for i in range(len(list)):
    print(heapq.heappop(list))

########################### END HEAP ############################