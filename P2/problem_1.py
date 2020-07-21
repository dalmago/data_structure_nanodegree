def recursive_sqrt_helper(target, start, end):
    # start and end are inclusive

    if start >= end:
        return start

    mid = (start + end) // 2

    # middle element is the floored square root of target if its square is len than or equal to the target and the
    # element + 1 squared is larger than the target
    if mid ** 2 <= target < (mid + 1) ** 2:
        return mid

    # discard lower half of the elements
    if mid ** 2 < target:
        return recursive_sqrt_helper(target, mid + 1, end)

    # discard upper half
    return recursive_sqrt_helper(target, start, mid - 1)


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    return recursive_sqrt_helper(number, 0, number)


print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (1 == sqrt(2)) else "Fail")
print("Pass" if (1 == sqrt(3)) else "Fail")
print("Pass" if (2 == sqrt(4)) else "Fail")
print("Pass" if (2 == sqrt(6)) else "Fail")
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (3 == sqrt(10)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (1643 == sqrt(27e5)) else "Fail")
