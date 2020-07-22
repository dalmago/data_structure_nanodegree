import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.
    The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min_value = ints[0]
    max_value = ints[0]

    for value in ints[1:]:  # no need to check first element
        if value > max_value:
            max_value = value
        if value < min_value:
            min_value = value

    return min_value, max_value


# Example Test Case of Ten Integers

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

print("Pass" if ((0, 0) == get_min_max([0])) else "Fail")
print("Pass" if ((-1, 1) == get_min_max([-1, 1])) else "Fail")
print("Pass" if ((-1, 1) == get_min_max([-1, 1, 1, 1, 1])) else "Fail")
print("Pass" if ((1, 1) == get_min_max([1, 1, 1, 1, 1])) else "Fail")
print("Pass" if ((1e-9, 5e10) == get_min_max([1e-9, 2, 4, 5e10])) else "Fail")
