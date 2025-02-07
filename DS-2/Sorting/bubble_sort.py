def bubbleSort(arr):
    for i in range(len(arr)-1):
        swap = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swap = True
        if not swap:
            break

    return arr

print(bubbleSort([2,4,11,10,5,1,0]))

# O(n^2) T
# O(1) S