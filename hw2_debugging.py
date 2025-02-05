import rand

def flawed_linear_search(arr, target):
    """
    A flawed linear search implementation for debugging practice.
    """
    for i in range(len(arr) - 1):
        if arr[i] == target:
            return i  # Correct case: target found

    return -1 

# Example usage (add this to test):
my_array = [10, 5, 20, 8, 12]

# Test cases:
print(f"Index of 20: {flawed_linear_search(my_array, 20)}")  # Should be 2
print(f"Index of 7: {flawed_linear_search(my_array, 7)}")   # Should be -1 

# Add more test cases, especially edge cases (empty array, target at beginning/end).
print(f"Index of 10: {flawed_linear_search(my_array, 10)}") # Should be 0
print(f"Index of 12: {flawed_linear_search(my_array, 12)}") # Should be 4
print(f"Index of 1: {flawed_linear_search([], 1)}") # Should be -1

def mergeSort(arr):
    if (len(arr) == 1):
        return arr

    half = len(arr)//2

    return recombine(mergeSort(arr[:half]), mergeSort(arr[half:]))

def recombine(leftArr, rightArr):
    leftIndex = 0
    rightIndex = 0
    mergeArr = [None] * (len(leftArr) + len(rightArr))
    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] < rightArr[rightIndex]:
            rightIndex += 1
            mergeArr[leftIndex + rightIndex] = leftArr[leftIndex]
        else:
            leftIndex += 1
            mergeArr[leftIndex + rightIndex] = rightArr[rightIndex]

    for i in range(rightIndex, len(rightArr)):
        mergeArr[leftIndex + rightIndex] = rightArr[i]
    
    for i in range(leftIndex, len(leftArr)):
        mergeArr[leftIndex + rightIndex] = leftArr[i]

    return mergeArr

arr = rand.random_array([None] * 20)
arr_out = mergeSort(arr)

print(arr_out)


