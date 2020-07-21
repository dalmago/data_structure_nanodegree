def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.
    O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an
    O(n) solution but it will not count as single traversal.

    Args:
       input_list(list): List to be sorted
    """
    # reference indexes marks the last 0 in the list and the first 2
    last_zero_idx = -1
    first_two_idx = len(input_list)  # after the end of the list

    idx = 0

    output_list = input_list.copy()  # not considering this copy in the algorithm's complexity

    # traverse
    while idx < first_two_idx:
        if output_list[idx] == 0:  # send zero to the beginning
            if idx == last_zero_idx + 1:  # if it is next to the last_zero_idx, only increment the index
                last_zero_idx += 1
            else:  # otherwise, swap elements
                # in this situation, we can assume input_list[last_zero_idx + 1] is always a 1, otherwise we would have
                # swapped or changed the reference indexes already
                output_list[idx], output_list[last_zero_idx + 1] = output_list[last_zero_idx + 1], output_list[idx]
                last_zero_idx += 1  # increment reference index of last zero in the list

        elif output_list[idx] == 2:
            if idx == first_two_idx - 1:  # if the 2 is just before the first_two_idx, just decrement the index and it's all set
                first_two_idx -= 1

            else:  # otherwise, send 2 to the beginning of the 2's sector
                output_list[idx], output_list[first_two_idx - 1] = output_list[first_two_idx - 1], output_list[idx]
                first_two_idx -= 1
                # since we don't know which element is going to be swapped with the idx, idx cannot be incremented yet
                continue

        idx += 1

    return output_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([2, 2, 0, 0, 2, 1, 0, 2, 2, 1, 1, 1, 0, 1, 2, 0, 2, 0, 1])
test_function([2, 1, 0])
test_function([2, 2, 2])
test_function([0, 0, 0])
test_function([0, 2, 0])
test_function([1, 2, 1])
test_function([0, 1, 0])
test_function([1, 0, 1])
test_function([1, 1])
test_function([0])
test_function([1])
test_function([2])
test_function([])

