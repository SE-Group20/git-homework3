import random

def random_array(size, min_val=1, max_val=20):  # More flexible: size, min, max
    """Generates a list of random integers."""
    return [random.randint(min_val, max_val) for _ in range(size)]