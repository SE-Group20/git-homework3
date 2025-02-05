import pytest
from hw2_debugging import mergeSort

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