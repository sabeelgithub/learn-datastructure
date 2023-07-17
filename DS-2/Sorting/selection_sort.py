array = [4,7,0,1,6,7,3]
print(array,'orginal array')
def selectionSort(arr):
    for i in range(len(arr)-1):
        min_pos = i
        for j in range(i+1,len(arr)):
            if arr[min_pos]>arr[j]:
                min_pos = j
        arr[i],arr[min_pos]=arr[min_pos],arr[i]
    
    return arr

selection_sorted = selectionSort(array)
print(selection_sorted,'selection sorted')

# O(n^2) T
# O(1) S