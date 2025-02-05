import re
from functools import cmp_to_key


def compare_chunk(x: str, y:str) -> int:
    # if different types, the numeric one is less
    if x.isdigit() and not y.isdigit():
        return -1
    if not x.isdigit() and y.isdigit():
        return 1
    
    # if both strings, compare lexicographically
    if not x.isdigit() and not y.isdigit():
        return 1 if x > y else -1
    
    # if both numbers:
    if x.isdigit() and y.isdigit():
        x_int = int(x)
        y_int = int(y)
        if x_int == y_int:
            return 0
        return 1 if x_int > y_int else -1
    
    return 0


def natural_compare_bad(x: str, y:str) -> int:
    """Compare two strings in a natural order."""
    chunks_x = []
    chunks_y = []

    current_chunk = ""
    current_chunk_type_is_digit = False
    for c in x:
        if c.isdigit():
            if not current_chunk_type_is_digit:
                chunks_x.append(current_chunk)
                current_chunk = ""
                current_chunk_type_is_digit = True
            current_chunk += c
        else:
            if current_chunk_type_is_digit:
                chunks_x.append(current_chunk)
                current_chunk = ""
                current_chunk_type_is_digit = False
            current_chunk += c

    chunks_x.append(current_chunk)

    current_chunk = ""
    current_chunk_type_is_digit = False
    for c in y:
        if c.isdigit():
            if not current_chunk_type_is_digit:
                chunks_y.append(current_chunk)
                current_chunk = ""
                current_chunk_type_is_digit = True
            current_chunk += c
        else:
            if current_chunk_type_is_digit:
                chunks_y.append(current_chunk)
                current_chunk = ""
                current_chunk_type_is_digit = False
            current_chunk += c

    chunks_y.append(current_chunk)

    for i in range(min(len(chunks_x), len(chunks_y))):
        cmp = compare_chunk(chunks_x[i], chunks_y[i])
        if cmp != 0:
            return cmp
    if len(chunks_x) < len(chunks_y):
        return -1
    elif len(chunks_x) > len(chunks_y):
        return 1
    
    return 0
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
    return natural_compare_bad(x, y)

def natural_sort(arr: list) -> list:
    """Sort a list of strings in natural order.

    Args:
        arr (list): The list of strings to sort.

    Returns:
        list: The sorted list of strings.
    """
    return sorted(arr, key=cmp_to_key(natural_compare))