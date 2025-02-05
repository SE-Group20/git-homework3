"""This module contains the mergeSort function."""
import rand_pkhare

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

def merge_sort(input_arr):
    """Sorts an array using the merge sort algorithm."""
    if len(input_arr) > 1:
        mid = len(input_arr) // 2
        left_arr = input_arr[:mid]
        right_arr = input_arr[mid:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        recombine(input_arr, left_arr, right_arr)

def recombine(arr, left_arr, right_arr):
    """Recombines two sorted arrays into a single sorted array."""
    left_index = 0
    right_index = 0
    arr_index = 0

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] <= right_arr[right_index]:
            arr[arr_index] = left_arr[left_index]
            left_index += 1
        else:
            arr[arr_index] = right_arr[right_index]
            right_index += 1
        arr_index += 1

    arr[arr_index:arr_index+len(left_arr[left_index:])] = left_arr[left_index:]
    arr[arr_index:arr_index+len(right_arr[right_index:])] = right_arr[right_index:]

random_array = rand_pkhare.random_array(20)
merge_sort(random_array) # Corrected
sorted_array = random_array # Corrected
print(sorted_array)
