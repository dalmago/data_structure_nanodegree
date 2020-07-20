import math

"""
Given an unsorted array Arr with n positive integers. Find the  𝑘𝑡ℎ  smallest element in the given array, using
Divide & Conquer approach.

Input: Unsorted array Arr and an integer k where 1 <= k <= n
Output: The kth smallest element of array Arr
"""

def fastSelect(arr, k):
    if len(arr) == 1:
        return arr[0]

    # break arr into n/5 groups namely Gi
    gs = []
    for i in range(math.ceil(len(arr)/5)):
        gs.append(arr[i * 5: (i+1) * 5])

    s = []  # median sets
    for gi in gs:  # for each G group
        gi.sort()  # sort
        s.append(gi[len(gi) // 2])  # find the middle position

    p = fastSelect(s, k//10)  # the "good" pivot element will be the median of S

    arr_less_p = []
    arr_equal_p = []
    arr_more_p = []
    for el in arr:  # partition the original arr into three sub-arrays
        if el < p:
            arr_less_p.append(el)
        elif el == p:
            arr_equal_p.append(el)
        else:  # el > p
            arr_more_p.append(el)

    if arr_less_p and k <= len(arr_less_p):
        return fastSelect(arr_less_p, k)
    elif arr_more_p and k > len(arr_less_p) + len(arr_equal_p):
        return fastSelect(arr_more_p, k - len(arr_less_p) - len(arr_equal_p))
    # else
    return p


Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42]
k = 5
print(fastSelect(Arr, k))        # Outputs 12

Arr = [5, 2, 20, 17, 11, 13, 8, 9, 11]
k = 5
print(fastSelect(Arr, k))        # Outputs 11

Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42, 99]
k = 10
print(fastSelect(Arr, k))        # Outputs 99
