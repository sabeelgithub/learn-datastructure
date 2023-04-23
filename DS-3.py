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


# ---------- min-heap ----------------

class MinHeap:
    def __init__(self):
        self.heap = []

    def parentIndex(self,i):
        return (i - 1) // 2

    def LeftChildIndex(self,i):
        return 2 * i + 1

    def RightChildIndex(self,i):
        return 2 * i + 2

    def get_min(self):
        if self.heap:
            return self.heap[0]
        else:
            return 'heap is empty'

    def insert(self,k):
        self.heap.append(k)
        i = len(self.heap)-1
        while i!=0 and self.heap[self.parentIndex(i)] > self.heap[i]:
            self.heap[self.parentIndex(i)],self.heap[i] = self.heap[i],self.heap[self.parentIndex(i)]
            i = self.parentIndex(i)
        return f'item {k} is added in heap'

    def min_heapify(self, i):
        l = self.LeftChildIndex(i)
        r = self.RightChildIndex(i)
        smallest = i
        if l < len(self.heap) and self.heap[l] < self.heap[smallest]:
            smallest = l
        if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
            smallest = r
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.min_heapify(smallest)

    def extract_min(self):
        if not self.heap:
            return 'heap is empty'
        if self.heap == 1:
            return self.heap.pop()
        else:
            temp = self.heap[0]
            self.heap[0] = self.heap[len(self.heap)-1]
            self.heap[len(self.heap)-1] = temp
            self.heap.pop()
            self.min_heapify(0)
            

            return temp
    
    def delete(self,i):
        if not self.heap:
            return 'heap is empty'
        else:
            temp = self.heap[i]
            self.heap[i] = self.heap[len(self.heap)-1]
            self.heap[len(self.heap)-1] = temp
            self.heap.pop()
            self.min_heapify(i)
            return f'item {temp} deleted'


        


    

    



min = MinHeap()
print(min.get_min())
print(min.heap)
print(min.insert(10))
print(min.heap)
print(min.get_min())
print(min.parentIndex(0))
print(min.insert(1))
print(min.heap)
print(min.get_min())
print(min.insert(100))
print(min.heap)
print(min.insert(5))
print(min.heap)
print(min.insert(50))
print(min.heap)
print(min.insert(0.5))
print(min.heap)
print(min.extract_min())
print(min.heap)
print(min.delete(1))
print(min.heap)

#----------------- max-heap -----------------

class MinHeap:
    def __init__(self):
        self.heap = []

    def parentIndex(self,i):
        return (i - 1) // 2

    def LeftChildIndex(self,i):
        return 2 * i + 1

    def RightChildIndex(self,i):
        return 2 * i + 2

    def get_max(self):
        if self.heap:
            return self.heap[0]
        else:
            return 'heap is empty'

    def insert(self,k):
        self.heap.append(k)
        i = len(self.heap)-1
        while i!=0 and self.heap[self.parentIndex(i)] < self.heap[i]:
            self.heap[self.parentIndex(i)],self.heap[i] = self.heap[i],self.heap[self.parentIndex(i)]
            i = self.parentIndex(i)
        return f'item {k} is added in heap'

    def min_heapify(self, i):
        l = self.LeftChildIndex(i)
        r = self.RightChildIndex(i)
        largest = i
        if l < len(self.heap) and self.heap[l] > self.heap[largest]:
            largest = l
        if r < len(self.heap) and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.min_heapify(largest)

    def extract_max(self):
        if not self.heap:
            return 'heap is empty'
        if self.heap == 1:
            return self.heap.pop()
        else:
            temp = self.heap[0]
            self.heap[0] = self.heap[len(self.heap)-1]
            self.heap[len(self.heap)-1] = temp
            self.heap.pop()
            self.min_heapify(0)
            

            return temp
    
    def delete(self,i):
        if not self.heap:
            return 'heap is empty'
        else:
            temp = self.heap[i]
            self.heap[i] = self.heap[len(self.heap)-1]
            self.heap[len(self.heap)-1] = temp
            self.heap.pop()
            self.min_heapify(i)
            return f'item {temp} deleted'


        


    

    



min = MinHeap()
print(min.get_max())
print(min.heap)
print(min.insert(10))
print(min.heap)
print(min.get_max())
print(min.parentIndex(0))
print(min.insert(1))
print(min.heap)
print(min.get_max())
print(min.insert(100))
print(min.heap)
print(min.insert(5))
print(min.heap)
print(min.insert(50))
print(min.heap)
print(min.insert(0.5))
print(min.heap)
print(min.extract_max())
print(min.heap)
print(min.delete(1))
print(min.heap)

########################### END HEAP ############################



############################ HEAP SORT ###########################

def heapify(arr,i):
    smallest = i
    l = 2 * i +1
    r = 2*i +2
    if l < len(arr) and arr[l] < arr[smallest]:
        smallest = l
    if r < len(arr) and arr[r] < arr[smallest]:
        smallest = r
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr,smallest)
    
    return arr


def heapSort(arr):
    for i in range(int(len(arr)/2)-1,-1,-1):
        heapify(arr,i)
    
    for i in range(len(arr)-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr,i)
        arr.reverse()
        return arr


print(heapSort([56,8,9,0,5]))


############################ END HEAP SORT #######################