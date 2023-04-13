
######################### SORTING ###########################

# ----------- BUBBLE SORTING ---------------#

def bubbleSort(arr):
    for i in range(len(arr)-1): # ----- O(n)
        for j in range(len(arr)-i-1): # -------- O(n)
            if arr[j] > arr[j+1]: # ------------------ O(1)
                arr[j],arr[j+1] = arr[j+1],arr[j]

    print(arr)
    return

jem = [1,3,6,8,9,2,4,7,5]
bubbleSort(jem)

# Time complexity = O(n^2)
# space complexity = O(1)

#------------ SELECTION SORT -----------------#

def selectionSort(arr):
    for i in range(len(arr)-1):
        min_pos = i
        for j in range(i+1,len(arr)):
            if arr[min_pos]> arr[j]:
                min_pos = j
        arr[i],arr[min_pos] = arr[min_pos],arr[i]
        print(arr)
    return

selectionSort([2,5,2,6,9,8,1,7])


# Time complexity - O(n^2)
# Space complexity - O(1)

#------------- INSERTION SORT-------------------#

def insertionSort(arr):
    for i in range(1,len(arr)):
        key = i
        while key>0 and arr[key-1] > arr[key]:
            arr[key-1],arr[key] = arr[key],arr[key-1]
            key -= 1

    print(arr)
    return
insertionSort([2,4,2,4,5,6,7,8,1]) 

# Time complexity - O(n^2)
# Space complexity - O(1)

# ---------------- BUCKET SORT ------------------------#


import math

def insertionSort(arr):
    for i in range(1,len(arr)):
        key = i
        while key>0 and arr[key-1] > arr[key]:
            arr[key-1],arr[key] = arr[key],arr[key-1]
            key -= 1

    print(arr)
    return arr

def BuketSort(listm):
    number_of_buckets = round(math.sqrt(len(listm)))
    max_value = max(listm)
    arr = []

    # creating buckets 
    for i in range(number_of_buckets):
        arr.append([])

    for j in listm:
        index_b = math.ceil(j*number_of_buckets/max_value)
        if index_b == 0:
            arr[index_b].append(j)
        else:
          arr[index_b-1].append(j)

    for i in range(number_of_buckets):
        arr[i] = insertionSort(arr[i])

    k = 0
    for i in range(number_of_buckets):
        for j in range(len(arr[i])):
            listm[k] = arr[i][j]
            k +=1
    
    print(arr)
    print(listm)
    return 

BuketSort([4,5,6,9,2,7,1,0,8,1])

# Time complexity - O(n^2)
# Space complexity - O(n)



# --------- MERGE SORT---------------#

# L1 = [1,2,3,4,5,6,78]
# print(max(L1))


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        mergeSort(left_arr)
        mergeSort(right_arr)
        i = 0
        j = 0
        k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i = i+1
                k = k+1
            else:
                arr[k] = right_arr[j]
                j = j+1
                k = k+1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i = i+1
            k = k+1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j = j+1
            k = k+1

    return arr
    
lo = mergeSort([2,0,6,7,8,3,5,6])
print(lo)

        
      



######################### END SORTING #######################