# list
lo = [1,2,3,'one','two','three',None,True,False]
for i in lo:
    if isinstance(i,int):
        print(i)

for i in lo:
    if isinstance(i,str):
        print(i) 

for i in lo:
    if isinstance(i,bool):
        print(i) 

for i in lo:
    if isinstance(i,float):
        print(i) 

for i in lo:
    if i is None:
        print(i)

# to delete all strings togther from list
lo = [1,2,3,'one','two','three',None,True,False,10.5,9.8]
lo = [i for i in lo if  not isinstance(i,str)]
print(lo)
# end        
# to delete all int togther from list
lo = [1,2,3,'one','two','three',None,True,False,10.5,9.8]
lo = [i for i in lo if  not isinstance(i,int)]
print(lo)
# end  
# to delete all booleans togther from list
lo = [1,2,3,'one','two','three',None,True,False,10.5,9.8]
lo = [i for i in lo if  not isinstance(i,bool)]
print(lo)
# end   
# to delete all float togther from list
lo = [1,2,3,'one','two','three',None,True,False,10.5,9.8]
lo = [i for i in lo if  not isinstance(i,float)]
print(lo)
# end                   
# end    

#dictionary
# two ways of creating dictionary using dict constructor
dict1 = dict(name='abu',age=12)
print(dict1)
dict2 = dict({'name':'abu','age':18})
print(dict2)
# end
# end  


# stack implementation using list
stack = []
# push can be done with append()
stack.append(1)
print(stack)
stack.append(10)
print(stack)
stack.append(100)
print(stack)
# pop can be done with pop
stack.pop()
print(stack)
# last value (top()) can be acced usig index
print(stack[-1])
# isEmpty() using leng()
if len(stack) == 0:
    print('stack is empty')



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

# stack implementation using deque class of collection moodule
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

# stack implementation using LifoQueue class of queue moodule    
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


# reversing string using stack
def reversing_string_with_stack(string):
    stack = []

    for i in string:
        stack.append(i)

    reversed_string = ''
    while stack:
         reversed_string += stack.pop()    

    return reversed_string

lo =reversing_string_with_stack('hello world')
print(lo)
# end





# stack
#------- traversing---------#
#(1).creating nodes
# we can create individual nodes like this
class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

# while creating a node intially its reference is given as null/none

        
node1 = Node(10)
print(node1) 

#(2) .to connect individual nodes wee need a  another class 
class LinkedList:
    def __init__(self):
        self.head = None
    def print_LL(self):
        if self.head is None:
            print('linked list is empty')
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

LL1 = LinkedList()
LL1.print_LL()

#---------insertion---------#
# add-begin

class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None
    def print_LL(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref 
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin(30)
LL1.print_LL()

        
        
# add-end
class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None
    def print_LL(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            n = self.head
            while n is not None:
                print(n.data,'---->',end="")
                n = n.ref 
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print('node is added at the empty linked list')
        else:
            n = self.head
            while n is not None:
                n = n.ref
            n = new_node


LL1 = LinkedList()
LL1.add_end(500)
LL1.add_begin(10)  
LL1.add_begin(20)
LL1.add_begin(30)
LL1.add_begin(40) 
LL1.print_LL()

        
        


             
         
        
# end