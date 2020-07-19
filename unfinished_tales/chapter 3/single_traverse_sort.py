"""
Write a function that takes an input array (or Python list) consisting of only 0s, 1s, and 2s, and sorts that array in a
single traversal.

Note that if you can get the function to put the 0s and 2s in the correct positions, this will automatically cause the
1s to be in the correct positions as well.
"""

def sort_012(input_list):
    # reference indexes
    last_zero_idx = -1
    first_two_idx = len(input_list)  # after the end of the list

    idx = 0

    # traverse
    while idx < first_two_idx:
        if input_list[idx] == 0:  # send zero to the beginning
            if idx == last_zero_idx + 1:
                idx += 1
                last_zero_idx += 1
            else:
                input_list[idx], input_list[last_zero_idx + 1] = input_list[last_zero_idx + 1], input_list[idx]
                last_zero_idx += 1

        elif input_list[idx] == 2:
            if idx == first_two_idx - 1:
                first_two_idx -= 1
                idx += 1
            else:
                input_list[idx], input_list[first_two_idx - 1] = input_list[first_two_idx - 1], input_list[idx]
                first_two_idx -= 1

        else:  # 1
            idx += 1

def test_function(test_case):
    sort_012(test_case)
    print(test_case)
    if test_case == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_case = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
test_function(test_case)

test_case = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
test_function(test_case)

test_case = [2, 2, 0, 0, 2, 1, 0, 2, 2, 1, 1, 1, 0, 1, 2, 0, 2, 0, 1]
test_function(test_case)

