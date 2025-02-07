def selectionSort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j

        arr[min_index],arr[i] =arr[i],arr[min_index]

    return arr

print(selectionSort([2,5,6,3,8,6,8]))

# O(n^2) T
# O(1) S