array = [4,7,0,1,6,7,3]
print(array,'orginal array')
# bubble sort 
def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    
    return arr
bubble_sorted = bubbleSort(array)
print(bubble_sorted,'bubble sorted array')

# O(n^2) T
# O(1) S