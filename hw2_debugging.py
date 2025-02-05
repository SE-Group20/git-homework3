import rand

def flawed_linear_search(arr, target):
    """
    A flawed linear search implementation for debugging practice.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Correct case: target found

    return -1 


my_array = [10, 5, 20, 8, 12] ## This doesn't throw Undefined names error
# Test cases:
print(f"Index of 20: {flawed_linear_search(my_array, 20)}")  # Should be 2
# Example usage (add this to test):
#my_array = [10, 5, 20, 8, 12] ## Should throw Undefined names error
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
    mergeArr = []  # Initialize as an empty list

    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] < rightArr[rightIndex]:
            mergeArr.append(leftArr[leftIndex])  # Use append
            leftIndex += 1
        else:
            mergeArr.append(rightArr[rightIndex])  # Use append
            rightIndex += 1

    # Add remaining elements (important!)
    mergeArr.extend(leftArr[leftIndex:])  # Use extend for efficiency
    mergeArr.extend(rightArr[rightIndex:])

    return mergeArr


arr = rand.random_array(20)
arr_out = mergeSort(arr)

print(arr_out)

