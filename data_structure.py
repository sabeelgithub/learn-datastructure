###################### LIST #######################

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
                   
################################# END LIST ####################    

########################### DICTIONARY ################################

# two ways of creating dictionary using dict constructor
dict1 = dict(name='abu',age=12)
print(dict1)
dict2 = dict({'name':'abu','age':18})
print(dict2)
# end
######################### END DICTIONARY ########################  

############################# STACK ############################

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


######################## END STACK ######################





##################################### LINKED LIST ########################################

#(1).singly linked list



                #------- traversing---------#
#creating nodes
# we can create individual nodes like this
class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

# while creating a node intially its reference is given as null/none

#to connect individual nodes wee need a  another class 
class LinkedList:
    def __init__(self):
        self.head = None
    def print_LL(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            n = self.head
            while n is not None:
                print(n.data,'---->',end=" ")
                n = n.ref 

                #---------insertion---------#
        # add-begin        
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

        # add-end
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print('node is added at the empty linked list')
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
            
             # in between nodes
        # add_after
    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
              break
            n = n.ref

        if n is None:
            print('node is not present in LL')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node 

        # add before    
    def add_before(self,data,x):
        if self.head is None:
            print('Linked list is empty')
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return 
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref

        if n.ref is None:
            print('node is not found')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print('linked list is not empty')

               #---------Deletion---------#

    def delete_begin(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            self.head = self.head.ref

    def delete_end(self):
        if self.head is None:
            print('linked list is empty')
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None   

    # delete at any position you want
    def delete_by_value(self,x):
        if self.head is None:
            print('Linked list empty,cant delete')
            return
        if x == self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print('node is not present')
        else:
            n.ref = n.ref.ref


    
             



LL1 = LinkedList()
LL1.add_end(50)
LL1.add_end(40)
LL1.add_end(30)
LL1.add_end(60)
LL1.add_after(35,30)
LL1.add_before(25,30)
LL1.add_begin(20)
LL1.add_begin(10)
LL1.insert_empty(100)
LL1.delete_begin()
LL1.delete_end()
LL1.delete_by_value(35)
LL1.delete_by_value(50)
LL1.delete_by_value(20)
LL1.print_LL()

#(2). doubly linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None

class doublyLL:
    def __init__(self):
        self.head = None
          
        #--------------- traversing-----------#

    # front-ward traversing
    def print_LL(self):
        if self.head == None:
            print('Linked list is empty')
        else:
            n = self.head
            while n is not None:
                print(n.data,'---->',end=" ")
            n = n.nref

    # back-ward traversing    
    def print_LL_reverse(self):
        if self.head == None:
            print('Linked list is empty')
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data,'------>',end =" ")
            n = n.pref

LL1 = doublyLL()
LL1.print_LL()


         
        
 
        
####################### END LINKED LIST ############################