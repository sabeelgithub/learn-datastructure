
######################### SORTING ###########################

# ----------- BUBBLE SORTING ---------------#

def bubbleSort(arr):
    for i in range(len(arr)-1): # ----- O(n)
        for j in range(len(arr)-i-1): # -------- O(n)
            if arr[j] > arr[j+1]: # ------------------ O(1)
                arr[j],arr[j+1] = arr[j+1],arr[j]

    print(arr)
    return

jem = [1,3,6,8,9,2,4,7,5]
bubbleSort(jem)

# Time complexity = O(n^2)
# space complexity = O(1)

#------------ SELECTION SORT -----------------#

def selectionSort(arr):
    for i in range(len(arr)-1):
        min_pos = i
        for j in range(i+1,len(arr)):
            if arr[min_pos]> arr[j]:
                min_pos = j
        arr[i],arr[min_pos] = arr[min_pos],arr[i]
        print(arr)
    return

selectionSort([2,5,2,6,9,8,1,7])


# Time complexity - O(n^2)
# Space complexity - O(1)

#------------- INSERTION SORT-------------------#

def insertionSort(arr):
    for i in range(1,len(arr)):
        key = i
        while key>0 and arr[key-1] > arr[key]:
            arr[key-1],arr[key] = arr[key],arr[key-1]
            key -= 1

    print(arr)
    return
insertionSort([2,4,2,4,5,6,7,8,1]) 

# Time complexity - O(n^2)
# Space complexity - O(1)

# ---------------- BUCKET SORT ------------------------#


import math

def insertionSort(arr):
    for i in range(1,len(arr)):
        key = i
        while key>0 and arr[key-1] > arr[key]:
            arr[key-1],arr[key] = arr[key],arr[key-1]
            key -= 1

    print(arr)
    return arr

def BuketSort(listm):
    number_of_buckets = round(math.sqrt(len(listm)))
    max_value = max(listm)
    arr = []

    # creating buckets 
    for i in range(number_of_buckets):
        arr.append([])

    for j in listm:
        index_b = math.ceil(j*number_of_buckets/max_value)
        if index_b == 0:
            arr[index_b].append(j)
        else:
          arr[index_b-1].append(j)

    for i in range(number_of_buckets):
        arr[i] = insertionSort(arr[i])

    k = 0
    for i in range(number_of_buckets):
        for j in range(len(arr[i])):
            listm[k] = arr[i][j]
            k +=1
    
    print(arr)
    print(listm)
    return 

BuketSort([4,5,6,9,2,7,1,0,8,1])

# Time complexity - O(n^2)
# Space complexity - O(n)



# --------- MERGE SORT---------------#

# L1 = [1,2,3,4,5,6,78]
# print(max(L1))


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        mergeSort(left_arr)
        mergeSort(right_arr)
        i = 0
        j = 0
        k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i = i+1
                k = k+1
            else:
                arr[k] = right_arr[j]
                j = j+1
                k = k+1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i = i+1
            k = k+1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j = j+1
            k = k+1

    return arr
    
lo = mergeSort([2,0,6,7,8,3,5,6])
print(lo)

# Time complexity - O(nlogn)
# Space complexity - O(n)    


#-------------- QUICK SORT -------------------------#

# pivot element as first element
def pivot_place(arr,first,last):
    pivot = arr[first]
    left = first + 1
    right = last
    while True:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while left <= right and arr[right] >= pivot:
            right = right-1
        if right < left:
            break
        else:
            arr[left],arr[right] = arr[right],arr[left]
    arr[first],arr[right] = arr[right],arr[first]
    return right
def quickSort(arr,first,last):
    if first < last:
        p = pivot_place(arr,first,last)
        quickSort(arr,first,p-1)
        quickSort(arr,p+1,last)
    
    return arr

check = quickSort([2,5,6,1,8,9,1,0,3,4],0,9)
print(check)

 # pivot element as last element

def pivot_place(arr,first,last):
    pivot = arr[last]
    left = first
    right = last-1
    while True:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while left <= right and arr[right] >= pivot:
            right = right -1
        if right < left :
            break
        else:
            arr[left],arr[right] = arr[right],arr[left]
    arr[left],arr[last] = arr[last],arr[left]
    return left

def quickSort(arr,first,last):
    if first < last:
        p = pivot_place(arr,first,last) # --------- O(n)
        quickSort(arr,first,p-1) # --------- T(n/2)
        quickSort(arr,p+1,last) # ----------- T(n/2)

    return arr

check = quickSort([2,5,6,9,3,5,1,9],0,7)
print(check)

# pivot element as random element

import random

def pivot_place(arr,first,last):
    rindex = random.randint(first,last)
    arr[rindex],arr[last] = arr[last],arr[rindex]
    pivot = arr[last]
    left = first
    right = last-1
    while True:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while left <= right and arr[right] >= pivot:
            right = right -1
        if right < left :
            break
        else:
            arr[left],arr[right] = arr[right],arr[left]
    arr[left],arr[last] = arr[last],arr[left]
    return left

def quickSort(arr,first,last):
    if first < last:
        p = pivot_place(arr,first,last)
        quickSort(arr,first,p-1)
        quickSort(arr,p+1,last)

    return arr

check = quickSort([2,5,6,9,3,5,1,9],0,7)
print(check)

# pivot element as median element

import statistics

def pivot_place(arr,first,last):
    low = arr[first]
    high = arr[last]
    med = arr[(first+last)//2]
    pivot_value = statistics.median([low,high,med])
    if pivot_value == low:
        pindex = first
    elif pivot_value == high:
        pindex = last
    else:
        pindex = med
    arr[pindex],arr[last] = arr[last],arr[pindex]
    pivot = arr[last]
    left = first
    right = last-1
    while True:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while left <= right and arr[right] >= pivot:
            right = right -1
        if right < left :
            break
        else:
            arr[left],arr[right] = arr[right],arr[left]
    arr[left],arr[last] = arr[last],arr[left]
    return left

def quickSort(arr,first,last):
    if first < last:
        p = pivot_place(arr,first,last)
        quickSort(arr,first,p-1)
        quickSort(arr,p+1,last)

    return arr

check = quickSort([2,5,6,9,3,5,1,9],0,7)
print(check)


# Time complexity - O(nlogn)
# Space complexity - O(n)    




######################### END SORTING #######################

############################ STACK ############################
# --------------- implementation using list -------------#

# implemntation of stack using list without fixed size

class Stack:
    def __init__(self):
        self.list = []
    
    def __str__(self):
        values = self.list.reverse()
        values = [str(i) for i in self.list]
        return '\n'.join(values)
    
    # is empty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    # push  
    def push(self,value):
        self.list.append(value)
        return f'item {value} added successfully'
    
    # pop
    def pop(self):
        if self.isEmpty():
            return 'there is no element in the list'
        else:
            return self.list.pop()
    
    # peek
    def peek(self):
        if self.list == []:
            return 'there is no any element in list'
        else:
            return self.list[len(self.list)-1]
        
    # delte  
    def delete(self):
        self.list = None

    
stack1 = Stack()
print(stack1.push(1))
print(stack1.push(2))
print(stack1.push(3))
print(stack1.pop())
print(stack1.peek())
print(stack1.list)
print(stack1)
print(stack1.isEmpty())

# implemntation of stack using list with fixed size

class Stack:
    def __init__(self,maxSize):
        self.maxSize = maxSize
        self.list = []
    
    def __str__(self):
        values = self.list.reverse()
        values = [str(i) for i in self.list]
        return '\n'.join(values)

    # is empty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    # push
    def push(self,value):
        if len(self.list)==self.maxSize:
            return 'cant add,list out of limit'
        else:
            self.list.append(value)
            return f'item {value} added successfully'

    # pop    
    def pop(self):
        if self.isEmpty():
            return 'cant delete,bcz its empty'
        else:
            return self.list.pop()
        
    # peek
    def peek(self):
        if self.isEmpty():
            return 'list is empty'
        else:
            return self.list[len(self.list)-1]
        
    # is Full
    def isFull(self):
        if self.maxSize == len(self.list):
            return True
        else:
            return False
        
    # accessing
    def access(self):
        if len(self.list)==0:
            return 'stack empty'
        else:
            for i in self.list:
                print(i)
            return 'done'
        
         
   
stack1 = Stack(4)
print(stack1.push(1))
print(stack1.push(2))
print(stack1.push(3))
print(stack1.push(4))
print(stack1.push(5))
print(stack1.pop())
print(stack1.peek())
print(stack1.isFull())
print(stack1.isEmpty())
print(stack1.list)
print(stack1)
print('------')
print(stack1.access())


# ------------------ implementation using linked list -------------

class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        n = self.head
        while n:
            yield n
            n = n.ref

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.data) for x in self.LinkedList]
        return '\n'.join(values)
         

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False
         
    def push(self,data):
        new_node =Node(data)
        new_node.ref = self.LinkedList.head
        self.LinkedList.head = new_node
        return f'item {data} added successfully'
    
    def pop(self):
        if self.LinkedList.head == None:
            return 'cant delete,its empty'
        else:
            node = self.LinkedList.head.data
            self.LinkedList.head = self.LinkedList.head.ref
            return node
        
    def peek(self):
        if self.isEmpty():
            return 'linked stack is empty'
        else:
            num = self.LinkedList.head.data
            return num
        
    def delete(self):
        self.LinkedList.head = None
       
        
obj = Stack()
print(obj.push(1))
print(obj.push(2))
print(obj.push(3))
print(obj)
print('---------')
print(obj.pop())
print(obj.isEmpty())
print('---------')
print(obj.peek())
print('---------')
#print(obj.delete())
print(obj)

#--------------- implentation using deque class of collection module-----------------------#

import collections
stack = collections.deque()
print(len(stack))
stack.append(1)
print(stack)
stack.append(20)
stack.append(50)
stack.append(100)
print(stack)
stack.pop()
print(stack)
print(stack[-1])
if len(stack) == 0:
    print('stack is empty')
else:
    print('stack is not empty')


# problem
stack = []
def push():
    if len(stack) == n:
        print('stack is full')
    else:
        add = int(input('enter number:'))
        stack.append(add)
        print(stack)

def pop():
    if len(stack) == 0:
        print('stack is empty')
    else:
        stack.pop()
        print('result is :',stack)

n = int(input('enter limit:'))

while True:
    print('eneter your choise 1 for push 2 for pop 3 for quit')
    choice = int(input('enter choice:'))
    if choice == 1:
        push()
    elif choice == 2:   
        pop()
    elif choice == 3:
        break
    else:
        print('invalid result')

try:
    stack = []
    def push():
        if len(stack)==n:
            print('stack is full')
        else:
            add = int(input('enter the item you want to add:'))
            stack.append(add)
            print(f'item {add} added successfully')
            print(stack)

    

    def pop():
        if len(stack) == 0:
            print('stack is empty,cant delete')
        else:
            stack.pop()
            print('afetr deleting',stack)
        

    n = int(input('enter the size of array:'))
    while True:
        print('enter the choices you want,1 for add,2 for delete,3 for quit')
        choice = int(input('enter the choice you want:'))
        if choice ==1:
            push()
        elif choice ==2:
            pop()
        elif choice ==3:
            break
        else:
            print('inavlid result')
except Exception as e:
    print(e)

# ---------- implementation using LifoQueue class of queue module-----------#


import queue
stack = queue.LifoQueue()
stack.put(1)
print(stack)
stack.put(20)
stack.put(30)
stack.put(40)
print(stack)
stack.put(68)
stack.get()
stack.get()
print(stack)

# reverse string using stack
def reverse_string(str):
    stack = []
    for i in str:
        stack.append(i)
    
    reverse =''
    while stack:
        reverse += stack.pop()
    return reverse

res = reverse_string('sabeel')
print(res)



############################ END STACK ########################