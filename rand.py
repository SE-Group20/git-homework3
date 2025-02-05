''' This module is for assigning random values to array '''
import random

def random_array(arr):
    """iterate through array and assign random int between 1-20"""
    for idx, _ in enumerate(arr):
        arr[idx] = random.randint(1, 20)  # Random number between 1 and 20
    return arr
