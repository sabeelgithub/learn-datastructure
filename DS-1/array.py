################################## ARRAY ###############################

#---------------------- 1D aary -------------------#

from array import *
# # (must be b, B, u, h, H, i, I, l, L, q, Q, f or d)
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


# reverse array
arr = [1,2,3,4,5]

# reverse using slicing
print(arr[::-1])

# using reverse method
arr.reverse()
print(arr)

# reverse array logic

arr = [1,4,5,7,3,2,5]

for i in range(len(arr)//2):
    arr[i],arr[len(arr)-i-1] = arr[len(arr)-i-1],arr[i]
    
print(arr)


################################## END ARRAY ###############################