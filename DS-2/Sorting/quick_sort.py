array = [4,7,0,1,6,7,3]
print(array,'orginal array')
# quick sort
# pivort 1st
def pivot_element(arr,first,last):
    pivot = arr[first]
    left = first + 1
    right = last
    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right]>=pivot:
            right -= 1

        if right < left:
            break
        else:
            arr[left],arr[right] = arr[right],arr[left]
    
    arr[first],arr[right] = arr[right],arr[first]

    return right

def quickSort(arr,first,last):
    if first < last:
        p = pivot_element(arr,first,last)
        quickSort(arr,first,p-1)
        quickSort(arr,p+1,last)
    return arr

n = len(array)-1
quicked_sort = quickSort(array,0,n)
print(quicked_sort,'quiked')

# pivot end 

def pivot_place(arr,first,last):
    pivot = arr[last]
    left = first
    right = last-1
    while True:
        while left <= right and arr[left] <= pivot:
            left +=1
        while left <= right and arr[right] >= pivot:
            right -=1
        if right < left:
            break
        else:
            arr[right],arr[left] = arr[left],arr[right]
    arr[last],arr[left]=arr[left],arr[last]
    return left

def mergeSort2(arr,first,last):
    if first < last:
        p = pivot_place(arr,first,last)
        mergeSort2(arr,first,p-1)
        mergeSort2(arr,p+1,last)
    return arr

n = len(array)-1
merged_sort2 = mergeSort2(array,0,n)
print(merged_sort2,'pivot last')

