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


# enumerate() method
fruits = ['apple', 'banana', 'cherry']
for index, value in enumerate(fruits):
    print(index, value)

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


    
             



SLL1 = LinkedList()
SLL1.add_end(50)
SLL1.add_end(40)
SLL1.add_end(30)
SLL1.add_end(60)
SLL1.add_after(35,30)
SLL1.add_before(25,30)
SLL1.add_begin(20)
SLL1.add_begin(10)
SLL1.insert_empty(100)
SLL1.delete_begin()
SLL1.delete_end()
SLL1.delete_by_value(35)
SLL1.delete_by_value(50)
SLL1.delete_by_value(20)
SLL1.print_LL()

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
        print()
        if self.head == None:
            print('Linked list is empty')
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data,'------>',end =" ")
                n = n.pref
    
    # insertion when linked list is empty
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print('Linked List is not empty')
    
    # add begin
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
    
    # add end
    def add_end(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n
    
    # add after
    def add_after(self,data,x):
        print('hell')
        if self.head is None:
            print('linked list is empty')
        else:
            print('gooys')
            n = self.head
            while n is not None:
                print('enterd')
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print('given node is not present in the list')
            else:
                print('chunk')
                new_node = Node(data)
                new_node.nref = n.nref
                n.nref = new_node
                if n.nref is not None:
                    n.nref.pref = new_node
                new_node.pref = n
    
    # add before
    def add_before(self,data,x):
        if self.head is None:
            print('Linked list is empty')
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            
            if n is None:
                print('given node is not present')
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node

    

    # delete begin
    def delete_begin(self):
        if self.head == None:
            print('Linked List is empty,cant delete')
            return
        if self.head.nref is None:
            self.head = None
            print('DLL is empty after deleting the node!')
        else:
            self.head = self.head.nref
            self.head.pref = None
    
    # delete end
    def delete_end(self):
        if self.head is None:
            print('Linked List is empty, cant delete')
            return
        if self.head.nref is None:
            self.head = None
            print('DLL is empty after deleteing node!')
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None 

    # delete by value
    def delete_by_value(self,x):
        if self.head == None:
            print('Linked List is empty')
            return
        if self.head.nref is None:
            if x == self.head.data:
                self.head = None
                print('item delted and List empty')
            else:
                print('given node not present in Linked List')
            return
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            return
        n = self.head
        while n.nref is not None:
            if x == n.data:
                break  
            n = n.nref
        if n.nref is not None:
            print('kery')
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        else:
            print('seen1')
            if n.data == x:
                print('seen 2')
                n.pref.nref = None
            else:
                print('node is not present in the Linked List')
                
        


DLL1 = doublyLL()
DLL1.insert_empty(5)
DLL1.add_end(10)
DLL1.add_begin(0)
DLL1.add_after(7,5) 
DLL1.add_before(3,5)
DLL1.delete_by_value(100)
DLL1.print_LL()
DLL1.print_LL_reverse()


        
####################### END LINKED LIST ############################



######################### LINEAR SEARCH #########################

def linearSearch(l,key):
    for idx,x in enumerate(l):
        if key == x:
            print('item found at :',idx+1)
            break
    else:
        print('item not found in the given list')

linearSearch([3,45,67,90],67)


list1 = [1,22,32,43,5,67,89]
print('this is the list for you :',list1)
try:
  num = int(input('enter the number you want to find:'))
  for idx,x in enumerate(list1):
    if num == x:
        print('item found at :',idx + 1)
        break

  else:
    print('item not found')
except ValueError as e:
    print(e)

########################## END ####################################

########################## BINARY SEARCH #########################
def binarySearch(num_list,key):
    start = 0
    end = len(num_list) - 1
    while start <= end:
        mid = (start + end)//2
        if num_list[mid] == key:
            return mid + 1
        elif num_list[mid] < key:
            start = mid + 1
        elif num_list[mid] > key:
            end = mid -1
    return -1
value = 5
pos = binarySearch([1,2,3,4,5],5)
if pos != -1:
    print('itm {0} found at {1} th position'.format(value,pos))
else:
    print(' not found')
 

############################# END BINARY SEARCH ############################



############################### STRING ################################

a = "Hello, World!"

# accessing and slicing
print(a[7])
print(a[2:5])
print(a[:5])
print(a[-11:-1])

# accessing with for loop
for i in a:
    print(i)

# len() = finding length of string
print(len(a))

# present or not
# in\not in
txt = "The best things in life are free!"
print('free' in txt)

if 'free' in txt:
    print('yes, \"free\" is present ')

print( 'boss' not in txt )

if 'boss' not in txt:
    print('no, \'boss\' not present')
else:
    print('yes, \'boss\' exists')

# upper() = making string in to uppercase
print(txt.upper())

# lower() = making string in to lowercase
print(txt.lower())

# stripe() = removing white space
aj = ' akmal ali '
print(aj.strip())

# replace() = replace a character with other 
print(aj.replace('k','j'))

# split() = splitting a string in to list of substring
print(aj.split(' '))

b = 'Hellow'
c = 'World'
print(b+' '+c)

# format()
aj_name = 'ajmal {}'
age = 22
print(aj_name.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {1} pieces of item {0} for {2} dollars."
print(myorder.format(quantity,itemno,price))

# escape character
print("i am \'mohammed\' sabeel")
print("i am 'mohammed' sabeel")


# capitalize() = convert the first character in to capital
mun = 'mUNAVAR'
print(mun.capitalize())

# casefold() = convert the strings in to lower case
print(mun.casefold())

# center() = used to center string by taking space specified inside center
chunk = mun.center(20)
print(len(chunk),chunk)

# count() = it return the number of specified strings
print(mun.count('m'))

# endswith() = it return the True if the string ends with specified character in the endswith()
print(mun.endswith('R'))

# expandtabs() = to increase tab size
print(mun.expandtabs())

# find() = find the starting index of specified item in the string,return -1 if the value not found
print(mun.find('NAVAR'))

# index() = find the starting index of specified item in the string ,it will raise an exception if value not found
print(mun.index('AVAR'))


# isalnum() = it return true if all characters in the string is alpha numeric
print(mun.isalnum())

# isalpha() = it return true if all characters in the string are alphabet
print(mun.isalpha())

lo = '101'
# isdecimal() = it return true if all characters in the string are decimal
print(lo.isdecimal())

# isdigit() = it return true if all characters in the string are digits
print(lo.isdigit())

# isdigit() = it return true if all characters in the string have white space
print(mun.isspace())


# removing all vowels in the strings

str = input('Enter the string :')

vowels_srtings = 'aeiouAEIOU'

for i in str:
    if i  in vowels_srtings:
        str = str.replace(i,'')

print('result after removing vowels :',str)

#removing all  characters in the string except vowels 

str = input('Enter the string :')

vowels_srtings = 'aeiouAEIOU'

for i in str:
    if i  not in vowels_srtings:
        str = str.replace(i,'')

print(' vowels in the string are:',str)


def removing_vowels(str):
    vowel_string = 'aeiouAEIOU'
    for i in str:
        if i in vowel_string:
            str = str.replace(i,'')

    
    print('result after removing voewls are :',str)
    return

removing_vowels('sabeel')


def finding_vowels(str):
    vowel_string = 'aeiouAEIOU'
    for i in str:
        if i not in vowel_string:
            str = str.replace(i,'')

    
    print('vowels are :',str)
    return

finding_vowels('sabeel')



# finding maximum lengthed word in the string


str = input('enter the the string you want :')

s=str.split()
max = 0
max_word = ''
for i in s:
    if len(i) > max:
        max = len(i)
        max_word = i

print('maximun length word is \'{}\' '.format(max_word),'and its length is {}.'.format(max)) 


def maximum_lengthed_word(str):
    s = str.split()
    max = 0
    max_word = ''
    for i in s:
        if len(i) > max:
            max = len(i)
            max_word = i
    
    print("maximum lengthed word is '{}' ".format(max_word),"and its length is {} ".format(max))
    return

maximum_lengthed_word('hellow welocome to python pogramming language')



# finding minimum lengthed word in the string

def maximum_lengthed_word(str):
    s = str.split()
    min = len(s[0])
    min_word = ''
    for i in s:
        if len(i) < min:
            min = len(i)
            min_word = i
    
    print("minimum lengthed word is '{}' ".format(min_word),"and its length is {} ".format(min))
    return

maximum_lengthed_word('hellow welocome to python pogramming language')
          
# reversing string
a = 'Hellow world'
print(a[::-1])


# palindrome workout

str = input('enter the string you want to check palindrome :')
if str == str[::-1]:
    print(str,'is palindrome')
else:
    print(str,'is not palindrome')


def palindrom_check(str):
    if str == str[::-1]:
        print(str,'is palindrome')
    else:
        print(str,'is not palindrome')

    return

palindrom_check('sabeel')



str = input('enter the string you want :')
rev_str = ''
for i in str:
    rev_str = i + rev_str

if str == rev_str:
    print(str,'is a palindrome')
else:
    print(str,'is not palindrome')


# Replaces each alphabet in a given string with another alphabet occurring at the n-th position from each of them.
def replace_with_nth_char(string,n):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    replaced_string = ''
    for i in string:
        if i in alphabet:
            is_lower = i.islower()
            i = i.lower()
            replaced_i = alphabet[(alphabet.index(i) + n)%26]
            if is_lower:
                replaced_string += replaced_i
            else:
                replaced_string += replaced_i.upper()
        else:
            replaced_string += i
    
    return replaced_string

print(replace_with_nth_char('helloo',1))


# add a word between splited word

str = 'Hello world'
s=str.split()
print(s)
result = ' hoi '.join(s)
print(result)

def split_and_add(str,add):
    s = str.split()
    new = ' '+add+' '
    result = new.join(s)
    print(result)
    return

split_and_add('hello world','hoi')




################################# END STRING ###########################


################################### ARRAY ###############################

#---------------------- 1D aary -------------------#

from array import *
arr1 = array('i',[1,2,3,4,5,6])
arr2 = array('d',[1.3,4.5,3.5])
print(arr1)
print(arr2)
print(type(arr1[1]))

# slicing
print(arr1[::-1])

# append() to add
arr1.append(7)
print(arr1)

# insert() to add
arr1.insert(7,8)
print(arr1)

# insert() to add
arr1.insert(0,0)
print(arr1)

# extend() to add
arr1.extend([9,10])
print(arr1)
print(arr1[0])

#remove() for removal
arr1.remove(10)
print(arr1)

#pop() for removel
arr1.pop()
print(arr1)
arr1.pop(2)
print(arr1)

#formlist() ,list has no this function ,to append a list
arr1.fromlist([100,101])
print(arr1)

# index() to find the index() specified item
print(arr1.index(101))

# reverse() to reverse array
arr1.reverse()
print(arr1)

# sum() to find the sum of array
print(sum(arr1))

# count() to find the count of specified item
print(arr1.count(1))

# tolist() to convert in list
print(arr1.tolist())   

# traversing  
def traverse_array(arr):
    for i in arr:
        print(i)
    return

traverse_array(arr1)

# accessing
def accssElement(array,index):
    if index >= len(array):
        print('no element in this index')
    else:
        print(array[index])
    return

accssElement(arr1,11)



# creation
print('choices are, 1 for int array,2  for float array')
try:
  choice = int(input('enter the choice you want :'))



  if choice == 1:
    length = int(input('enter the length you want to add:'))
    arrays = array('i',[])
    print(arrays)
    print(type(arrays))
    for i in range(length):
        num = int(input('enter number:'))
        arrays.append(num)


  if choice == 2:
    length = int(input('enter the length you want to add:'))
    arrays = array('d',[])
    print(arrays)
    print(type(arrays))
    for i in range(length):
        num = float(input('enter item:'))
        
        arrays.append(num)

    print(arrays)

except Exception as e:
    print(e)


# searching 
def search_array(array,value):
    for idx,x in enumerate(array):
        if x == value:
            print('item {}'.format(x),'found at {} position'.format(idx))
            break
    else:
        print('item not found')

    return
search_array(arr2,4.5)


# sum

arr1 = array('i',[1,2,3,4,5,6,9])
found = False  # Initialize a flag to False

for i in range(len(arr1)):
    for j in range(i + 1, len(arr1)):
        if arr1[i] + arr1[j] == 10:
            print("Two numbers with sum 10 are:", arr1[i], arr1[j])
            found = True  # Set the flag to True if a pair is found

if not found:
    print("No such numbers found.")



arr1 = array('i',[1,2,3,4,5,6,5])

newarr = array('i',[])
print(newarr)
print('ko')
found = False
for i in arr1:
    sub = 10 - i
    if sub in newarr:
        print('numbers are {},{}'.format(i,sub))
        found = True
    else:
        newarr.append(i)
print(newarr)        

if not found:
    print('no')


################################## END ARRAY ###############################

################################### RECURSION ################################

def Factorial(n):
   assert n >=0 and int(n) == n,'the number must be positive integer'
   if n in [0,1]:
      return 1
   else:
      return n * Factorial(n-1)
    
print(Factorial(5))

################################### END ######################################