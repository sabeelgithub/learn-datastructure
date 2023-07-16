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