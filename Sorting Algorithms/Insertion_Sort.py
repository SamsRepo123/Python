
# Python Program to implement Insertion Sort

def insertionSort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        n = arr[i]

        # Move elements of arr[0..i-1], that are greater than 'n', move one position ahead of current postion
        j = i-1
        while j >= 0 and n < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = n

#
arr = [10, 44, 38, 92, 2, 76]
insertionSort(arr)
for i in range(len(arr)):
    print("%d" %arr[i])