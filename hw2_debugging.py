from .rand import random_array


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_arr = mergeSort(arr[:mid])
    right_arr = mergeSort(arr[mid:])
    return recombine(left_arr, right_arr)

def recombine(leftArr, rightArr):
    leftIndex = 0
    rightIndex = 0
    mergeArr = []  # Start with an empty list and append

    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] <= rightArr[rightIndex]: # <= handles duplicates correctly
            mergeArr.append(leftArr[leftIndex])
            leftIndex += 1
        else:
            mergeArr.append(rightArr[rightIndex])
            rightIndex += 1

    # Add any remaining elements from left or right (only one of these will execute)
    mergeArr.extend(leftArr[leftIndex:])  # Efficiently adds the rest
    mergeArr.extend(rightArr[rightIndex:])

    return mergeArr

arr = random_array([None] * 20)
arr_out = mergeSort(arr)

print(arr_out)
