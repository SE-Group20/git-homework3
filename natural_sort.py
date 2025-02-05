import re
from functools import cmp_to_key

def natural_compare_good(x: str, y:str) -> int:
    """Compare two strings in a natural order.

    Args:
        x (str): The first string.
        y (str): The second string.

    Returns:
        int: -1 if x < y, 1 if x > y, 0 if x == y.
    """
    # Split the strings into parts of digits and non-digits
    x_parts = re.split(r'(\d+)', x)
    y_parts = re.split(r'(\d+)', y)

    # Compare each part
    for x_part, y_part in zip(x_parts, y_parts):
        # If both parts are digits, compare them as integers
        if x_part.isdigit() and y_part.isdigit():
            if int(x_part) < int(y_part):
                return -1
            elif int(x_part) > int(y_part):
                return 1
        else:
            # Otherwise, compare them as strings
            if x_part < y_part:
                return -1
            elif x_part > y_part:
                return 1

    # If all parts are equal, the strings are equal
    return 0

def natural_compare(x: str, y:str) -> int:
    return natural_compare_good(x, y)

def natural_sort(arr: list) -> list:
    """Sort a list of strings in natural order.

    Args:
        arr (list): The list of strings to sort.

    Returns:
        list: The sorted list of strings.
    """
    return sorted(arr, key=cmp_to_key(natural_compare))