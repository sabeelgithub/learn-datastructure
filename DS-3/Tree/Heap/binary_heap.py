# minheap
class MinHeap:
    def __init__(self):
        self.heap = []
    
    def ParentIndex(self,i):
        return (i-1)//2
    
    def lchild(self,i):
        return 2*i + 1
    
    def rchild(self,i):
        return 2*i + 2
    
    def get_min(self):
        if self.heap is None:
            print('min heap is empty')
            return
        else:
            return self.heap[0]
    
    def Insert(self,k):
        self.heap.append(k)
        i = len(self.heap)-1
        while i > 0 and self.heap[self.ParentIndex(i)] > self.heap[i]:
            self.heap[self.ParentIndex(i)],self.heap[i] = self.heap[i],self.heap[self.ParentIndex(i)]
            i = self.ParentIndex(i)
        return f'item {k} is added successfully'
    
    def min_heapify(self,i):
        l = self.lchild(i)
        r = self.rchild(i)
        smallest = i
        if l < len(self.heap) and self.heap[l] < self.heap[smallest]:
            smallest = l
        if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
            smallest = r
        if smallest != i:
            self.heap[smallest],self.heap[i] = self.heap[i],self.heap[smallest]
            self.min_heapify(smallest)

    def extract_min(self):
        if self.heap is None:
            print('cant extract min,because its empty min heap')
            return
        elif len(self.heap) == 1:
            return self.heap.pop()
        else:
            temp = self.heap[0]
            self.heap[0] = self.heap[len(self.heap)-1]
            self.heap[len(self.heap)-1] = temp
            self.heap.pop()
            self.min_heapify(0)
            return temp
        
    def delete(self,i):
        if self.heap is None:
            print('cant delete ,because our min heap is empty')
            return
        else:
            if i <= len(self.heap):
                temp = self.heap[i]
                self.heap[i] = self.heap[len(self.heap)-1]
                self.heap[len(self.heap)-1] = temp
                self.heap.pop()
                self.min_heapify(i)
                print(f'item with index {i} is deleted successfully')
            else:
                print('out of index')


 

min = MinHeap()
print(min.Insert(5))
print(min.Insert(10))
print(min.Insert(15))
print(min.Insert(20))
print(min.Insert(2))
print(min.extract_min())
min.delete(0)
print(min.heap)
print(min)


# maxheap
class Maxheap:
    def __init__(self):
        self.heap = []
    def ParentIndex(self,i):
        return (i-1)//2
    def lchild(self,i):
        return 2*i + 1
    def rchild(self,i):
        return 2*i + 2
    def get_max(self):
        if self.heap is None:
            print('cant get maximum,because its empty')
            return
        else:
            return self.heap[0]
    def insert(self,k):
        self.heap.append(k)
        i = len(self.heap)-1
        while i > 0 and self.heap[self.ParentIndex(i)] < self.heap[i]:
            self.heap[self.ParentIndex(i)],self.heap[i] = self.heap[i],self.heap[self.ParentIndex(i)],
            i = self.ParentIndex(i)
        return f'item {k} is added on max-heap'
    
    def max_heapify(self,i):
        l = self.lchild(i)
        r = self.rchild(i)
        largest = i
        if l < len(self.heap) and self.heap[l]>self.heap[largest]:
            largest = l
        if r < len(self.heap) and self.heap[r]>self.heap[largest]:
            largest = r
        if largest != i:
            self.heap[i],self.heap[largest] = self.heap[largest],self.heap[i],
            self.max_heapify(largest)
    
    def extract_max(self):
        if self.heap is None:
            print('max-heap is empty')
            return
        elif len(self.heap) == 1:
           return self.heap.pop()
        else:
            temp = self.heap[0]
            self.heap[0] = self.heap[len(self.heap)-1]
            self.heap[len(self.heap)-1] = temp
            self.heap.pop()
            self.max_heapify(0)
            return temp
        
    def delete(self,i):
        if self.heap is None:
            print('cant delete,max-heap is already empty')
            return
        else:
            if self.heap[i]:
                temp = self.heap[i]
                self.heap[i] = self.heap[len(self.heap)-1]
                self.heap[len(self.heap)-1] = temp
                self.heap.pop()
                self.max_heapify(i)
                print(f'item with index {i} is deleted')
            else:
                print('no such item in this max-heap')


max = Maxheap()
print(max.insert(5))
print(max.insert(2))
print(max.insert(15))
print(max.insert(20))
print(max.get_max())
print(max.extract_max())
print(max.delete(1))
print(max.heap)



# insertion
# O(logn)-T
# O(1)-S
# deletion
# O(logn)-T
# O(1)-S
# find min and max
# O(1)-T
# O(1)-S




        

    

        