############# LIST ################
# list can be created using list() constructor
list01 = list()
print(list01)  # empty list created

# iterables can be passed to list()
list02 = list("Hlo")
list03 = list([1,2,3])
list04 = list((2,"k",4))
list05 = list({1,3,4,"lo"})
list06 = list({"one":1,"two":'two'})

thislist = list(('hlo','hot','koi'))
print(thislist)

#slicing
print(thislist[0:2])
print(thislist[:2])
print(thislist[:])
print(thislist[0:])
print(thislist[-3:])
print(thislist[-3:-1])

# assigning
thislist[0] = 6
print(thislist)

# append() => append method used for add a value at end of the list
thislist.append(9)
thislist.append(True)
thislist.append(None)
thislist.append('boss')
print(thislist)

# insert() => insert method is used for adding an element on position we want ,insert(specify index,specify element to add)
thislist.insert(0,8)
thislist.insert(1,False)
thislist.insert(2,None)
thislist.insert(4,'sabi')
print(thislist)

# extend() => using extend we can add elements of iterables to list
thislist.extend(('anshu','pottathyee',6))
thislist.extend(['anshu','pottathyee',6])
thislist.extend({'anshu','pottathyee',6})
thislist.extend({'name':'sabeel','age':22})
thislist.extend('iterable')
print(thislist)

# remove() = > remove method using for removing an element from list,we can specify elements inside remove method
thislist.remove('name')
thislist.remove('age')
thislist.remove(False)
thislist.remove(True)
print(thislist)


# pop() => pop method is used for removing elements from list by specifyind index number of the list
thislist.pop() # pop method without specify any index will remove last elements of the list
thislist.pop(0)
print(thislist)

""" sort() => sort method is used for sorting list ,
in the case of integer list it order in ascendign order,
in the case of integer list it order in alpha neumerical asceding order,
revers=True is used for desending
this mehtod not work in the case of list with multiple data types """

thislist.sort()
print(thislist)

thislist.sort(reverse=True)
print(thislist)

# Q-Remove all integers in the list
li = [1,2,3,"f",4,5]

li = [i for i in li if not isinstance(i,int)]




# isinstance()
my_list = ['apple', 123, 'orange', 3.14, True, 'banana', 'grape']
my_list = [item for item in my_list if not isinstance(item, str)]
print(my_list)


# index() : it returns the index number specified value
list1 = [1,2,3,4,5,6,'one']
print(list1.index('one'))

# count() and sum()
listm = [1,1,2,3,4]
print(listm.count(1))
print(sum(listm))
l = [1,2,3,4,5,6,7]
print(max(l))

list1 = [1,2,3,4,5]
list1 = [str(i) for i in list1]
print(list1)

# list comprehension
list = ['apple','grape','watermelon','banana']
newlist = []

for i in list:
    newlist.append(i)

print(newlist)    

aginlist = [x for x in list if x == 'apple']
print(aginlist)

solist  = [x for x in list if x != 'apple']
print(solist)

top = [x for x in list if 'b' in x]
print(top)

# copy()
print(thislist)
new = thislist.copy()
print(new)
# reverse()
new.reverse()
print(new)

del thislist[0]
del thislist[1]
del thislist[2]
del thislist[3]
del thislist[4]
print(thislist)

thislist.clear()
print(thislist)

setnew1 = [1,3,'one',True]
setnew2 = [1,3,'one',True]


setnew = setnew1 + setnew2
print(setnew)
setnew = setnew1 * 3
print(setnew)

# in to tuple
into_tuple = tuple(setnew1)
print(into_tuple)

# in to set
into_set = set(setnew2)
print(into_set)


myList = ["John", "Peter", "Vicky"]

x = ' '.join(myList)

print(x)

# end



################ END LIST #################