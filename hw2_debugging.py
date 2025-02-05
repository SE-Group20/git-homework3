"""This module is to sort an array using merge sort"""
import rand

def merge_sort(arr):
    """split array in half and recombine sorted halves"""
    if len(arr) == 1:
        return arr

    half = len(arr)//2
    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))

def recombine(left_arr, right_arr):
    """merging sorted halves"""
    left_index = 0
    right_index = 0
    merge_array = []
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_array.append(left_arr[left_index])
            left_index += 1
        else:
            merge_array.append(right_arr[right_index])
            right_index += 1

    merge_array.extend(left_arr[left_index:])
    merge_array.extend(right_arr[right_index:])
    return merge_array

#uraycha - selection sort:
def selection_sort(arr):
    '''Finds minimum element from unsorted part and swaps'''
    for i, _ in enumerate(arr):
        min_idx = i  # Find the minimum element in the unsorted part of the array
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr_in = rand.random_array([None] * 20)
arr_out = merge_sort(arr_in)
arr_in_sel_sort = rand.random_array([None] * 10)
arr_sel_sort = selection_sort(arr_in)
print(arr_out)
