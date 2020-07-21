def recursive_arr_search(arr, value, start, stop):
    # stop is inclusive

    # base case
    if start >= stop:
        if arr[start] == value:
            return start
        return -1

    mid = (start + stop) // 2
    mid_el = arr[mid]

    if mid_el == value:  # found the element
        return mid

    if mid_el > arr[start]:  # first half is sorted
        # if the target value is larger than the middle element and the first half of the array is sorted, than the
        # target could only be in the second half of the array and we discard the first half. Also, if the value is
        # smaller than the first element, we can discard the first half as well
        if value > mid_el or value < arr[start]:
            return recursive_arr_search(arr, value, mid + 1, stop)

        else:  # target value is smaller than middle element
            return recursive_arr_search(arr, value, start, mid - 1)

    else:  # second half is sorted:
        # if the target value is smaller than the middle element and the second half of the array is sorted, than the
        # target could only be in the first half of the array. The same happens if the target value is larger than the
        # last element of the array
        if value < mid_el or value > arr[stop]:
            return recursive_arr_search(arr, value, start, mid - 1)

        else:
            return recursive_arr_search(arr, value, mid + 1, stop)


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array
    Runtime complexity must be in the order of O(log n)

    Args:
       input_list(array): Input array to search
       number(int): The target
    Returns:
       int: Index or -1
    """
    if len(input_list) == 0:
        return -1

    return recursive_arr_search(input_list, number, 0, len(input_list) - 1)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[5, 6, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[5, 6, 8, 9, 10, 1, 2, 3, 4], 3])
test_function([[6, 7, 8, 9, 1, 2, 3, 4, 5], 6])
test_function([[6, 7, 8, 9, 1, 2, 3, 4, 5], 3])

test_function([[8, 9, 10, 1, 2, 3, 4, 6, 7], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[6], 10])
test_function([[6], 6])
test_function([[], 2])
