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
# append()
thislist.append(9)
thislist.append(True)
thislist.append(None)
thislist.append('boss')
print(thislist)
# insert() 
thislist.insert(0,8)
thislist.insert(1,False)
thislist.insert(2,None)
thislist.insert(4,'sabi')
print(thislist)
# extend()
thislist.extend(('anshu','pottathyee',6))
thislist.extend(['anshu','pottathyee',6])
thislist.extend({'anshu','pottathyee',6})
thislist.extend({'name':'sabeel','age':22})
thislist.extend('iterable')
print(thislist)
# remove()
thislist.remove('name')
thislist.remove('age')
print(thislist)
# pop()
thislist.pop()
thislist.pop(0)
thislist.remove(False)
thislist.remove(True)

print(thislist)
for i in thislist:
    if type(i)==int:
        thislist.remove(i)

for i in thislist:
    if isinstance(i,int):
        thislist.remove(i)

for i in thislist:
    if i == None:
        thislist.remove(i)


thislist.sort()
print(thislist)

thislist.sort(reverse=True)
print(thislist)

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