"""
You are given an array arr having n integers. You have to find the maximum sum of contiguous subarray among all the
possible subarrays.
This problem is commonly called as Maximum Subarray Problem. Solve this problem in O(n logn) time, using Divide and
Conquer approach.
"""

def maxCrossingSum(arr, start, mid, stop):  # O(n)
    max_left = arr[mid]
    max_right = arr[mid + 1]

    left_idx = mid - 1
    right_idx = mid + 2
    left_sum = max_left
    right_sum = max_right

    while left_idx >= start:
        left_sum += arr[left_idx]

        if left_sum > max_left:
            max_left = left_sum

        left_idx -= 1

    while right_idx <= stop:
        right_sum += arr[right_idx]

        if right_sum > max_right:
            max_right = right_sum

        right_idx += 1

    return max_left + max_right


def maxSubArrayRecurs(arr, start, stop):  # T(n)
    if start == stop:
        return arr[start]

    mid_idx = (start + stop) // 2

    l = maxSubArrayRecurs(arr, start, mid_idx)  # T(n/2)
    r = maxSubArrayRecurs(arr, mid_idx + 1, stop)  # T(n/2)
    c = maxCrossingSum(arr, start, mid_idx, stop)

    return max(l, r, c)


def maxSubArray(arr):
    """
    param: An array `arr`
    return: The maximum sum of the contiguous subarray.
    No need to return the subarray itself.

    T(n) = 2 * T(n/2) + O(n) = O(n log(n))
    """
    return maxSubArrayRecurs(arr, 0, len(arr) - 1)


# Test your code
arr = [-2, 7, -6, 3, 1, -4, 5, 7]
print("Maximum Sum = ", maxSubArray(arr))  # Outputs 13

# Test your code
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum Sum = ", maxSubArray(arr))  # Outputs 6

# Test your code
arr = [-4, 14, -6, 7]
print("Maximum Sum = ", maxSubArray(arr))  # Outputs 15

# Test your code
arr = [-2, 1, -3, 5, 0, 3, 2, -5, 4]
print("Maximum Sum = ", maxSubArray(arr))  # Outputs 10

# Test your code
arr = [-2, -5, 6, -2, -3, 1, 5, -6]
print("Maximum Sum = ", maxSubArray(arr))  # Outputs 7
