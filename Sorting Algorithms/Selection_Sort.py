
# Python Program to implement Selection Sort

import sys
arr = [98, 72, 64, 55, 28, 36, 54]
# Traverse through all array elements
for i in range(len(arr)):

    # Find the minimum element in remaining unsorted array
    min_inx = i
    for j in range(i+1, len(arr)):
        if arr[min_inx] > arr[j]:
            min_inx = j

    # Swap the found minimum element with the first
    arr[i], arr[min_inx] = arr[min_inx], arr[i]

# Printing Sorted List
print("Sorted Array")
for i in range(len(arr)):
    print("%d"%arr[i])