
def mergesort(items):
    # Base case, a list of 0 or 1 items is already sorted
    if len(items) <= 1:
        return items

    # Otherwise, find the midpoint and split the list
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    # Call mergesort recursively with the left and right half
    left = mergesort(left)
    right = mergesort(right)

    # Merge our two halves and return
    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Move through the lists until we have exhausted one
    while left_index < len(left) and right_index < len(right):
        # If left's item is larger, append right's item
        # and increment the index
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        # Otherwise, append left's item and increment
        else:
            merged.append(left[left_index])
            left_index += 1

    # Append any leftovers. Because we've broken from our while loop,
    # we know at least one is empty, and the remaining:
    # a) are already sorted
    # b) all sort past our last element in merged
    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.
    The expected time complexity is O(nlog(n))

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    ordered_list = mergesort(input_list)  # sort input list using merge sort, larger digits first - O(N log(N))

    first_number = 0
    second_number = 0

    for idx, value in enumerate(ordered_list):  # O(N)
        # the ordered elements are going to be added one each number, larger value first
        if idx % 2 == 0:  # even indexes
            first_number *= 10  # Since a new digit is going to be added to the end of the number, multiply by 10
            first_number += value
        else:  # odd indexes
            second_number *= 10
            second_number += value

    return first_number, second_number


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[0, 0], [0, 0]])
test_function([[1, 0], [1, 0]])
test_function([[], [0, 0]])
test_function([[9, 8, 9, 8, 9, 0], [998, 980]])
