########################## BINARY SEARCH #########################
def binarySearch(arr,key):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == key:
            return mid + 1
        elif  key < arr[mid]:
            end = mid -1
        elif key > arr[mid]:
            start = mid + 1
    return -1
value = 5
pos = binarySearch([1,2,3,4,5],5)
if pos != -1:
    print('itm {0} found at {1} th position'.format(value,pos))
else:
    print(' not found')
 

############################# END BINARY SEARCH ############################