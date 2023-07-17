array = [4,7,0,1,6,7,3]
print(array,'orginal array')
# insertion sort
def insertionSort(arr):
    for i in range(len(arr)-1):
        key = i
        while i>0 and arr[key-1]>arr[key]:
            arr[key-1],arr[key]=arr[key],arr[key-1]
            i -= 1
    return arr
insertion_sorted = insertionSort(array)
print(insertion_sorted,'insertion sorted')

# O(n^2) T
# O(1) S