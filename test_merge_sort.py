"""This module contains the unit tests for the mergeSort function."""

import random
from hw2_debugging import merge_sort

def test_merge_sort_empty_array():
    """Tests mergeSort with an empty array."""
    arr = []
    merge_sort(arr)
    assert not arr

def test_merge_sort_sorted_array():
    """Tests mergeSort with an already sorted array."""
    arr = [1, 2, 3, 4, 5]
    merge_sort(arr)
    assert arr == [1, 2, 3, 4, 5]

def test_merge_sort_unsorted_array():
    """Tests mergeSort with an unsorted array."""
    arr = [5, 2, 8, 1, 9, 4]
    merge_sort(arr)
    assert arr == [1, 2, 4, 5, 8, 9]

def test_merge_sort_duplicate_elements():
    """Tests mergeSort with an array containing duplicate elements."""
    arr = [5, 2, 8, 1, 9, 4, 2, 5]
    merge_sort(arr)
    assert arr == [1, 2, 2, 4, 5, 5, 8, 9]

def test_merge_sort_negative_numbers():
    """Tests mergeSort with an array containing negative numbers."""
    arr = [-5, 2, -8, 1, 9, -4]
    merge_sort(arr)
    assert arr == [-8, -5, -4, 1, 2, 9]

def test_merge_sort_large_array():
    """Tests mergeSort with a large random array."""
    arr = [random.randint(0, 1000) for _ in range(1000)]
    sorted_arr = sorted(arr)
    merge_sort(arr)
    assert arr == sorted_arr
