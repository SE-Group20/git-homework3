from hw2_debugging import merge_sort

def test_merge_sort():
    #uraycha
    arr = [6,3,9,0]
    assert merge_sort(arr) == [0,3,6,9]

def test_reverse_sorted_array():
    #uraycha
    arr = [10,9,8,7,6]
    assert merge_sort(arr) == [6,7,8,9,10]

def test_duplicate_values():
    #uraycha
    arr = [7,5,3,7,5,5]
    assert merge_sort(arr) == [3,5,5,5,7,7]