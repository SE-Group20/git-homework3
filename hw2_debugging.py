import rand
import pytest

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

# Test cases using pytest
def test_merge_sort_empty_array():
    arr = []
    mergeSort(arr)
    assert arr == []  # Empty array should remain empty

def test_merge_sort_sorted_array():
    arr = [1, 2, 3, 4, 5]
    mergeSort(arr)
    assert arr == [1, 2, 3, 4, 5]  # Already sorted array should remain the same

def test_merge_sort_unsorted_array():
    arr = [5, 2, 8, 1, 9, 4]
    mergeSort(arr)
    assert arr == [1, 2, 4, 5, 8, 9]  # Unsorted array should be sorted

def test_merge_sort_duplicate_elements():
    arr = [5, 2, 8, 1, 9, 4, 2, 5]
    mergeSort(arr)
    assert arr == [1, 2, 2, 4, 5, 5, 8, 9]

def test_merge_sort_negative_numbers():
    arr = [-5, 2, -8, 1, 9, -4]
    mergeSort(arr)
    assert arr == [-8, -5, -4, 1, 2, 9]

def test_merge_sort_large_array():  # Test with a larger array
    import random
    arr = [random.randint(0, 1000) for _ in range(1000)]
    sorted_arr = sorted(arr)  # Use Python's built-in sort for comparison
    mergeSort(arr)
    assert arr == sorted_arr
