import pytest

from .hw2_debugging import mergeSort

class TestMergeSort:
    def test_merge_sort(self):
        assert mergeSort([1, 2, 3]) == [1, 2, 3]
        assert mergeSort([3, 2, 1]) == [1, 2, 3]
        assert mergeSort([1, 3, 2]) == [1, 2, 3]
        assert mergeSort([2, 1, 3]) == [1, 2, 3]
        assert mergeSort([2, 3, 1]) == [1, 2, 3]
        assert mergeSort([3, 1, 2]) == [1, 2, 3]

