
def heapsort(arr):
    # First convert the array into a maxheap by calling heapify on each node, starting from the end
    # Now that you have a maxheap, you can swap the first element (largest) to the end (final position)
    # and make the array minus the last element into maxheap again.
    # Continue to do this until the whole array is sorted

    # Build a maxheap.
    for i in range(len(arr) - 1, -1, -1):
        heapify(arr, len(arr), i)

    for i in range(len(arr) - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]  # swap
        heapify(arr, i, 0)


def heapify(arr, n, i):
    """
    :param: arr - array to heapify
    n -- number of elements in the array
    i -- index of the current node

    Converts an array (in place) into a maxheap, a complete binary tree with the largest values at the top

    Using i as the index of the current node, find the 2 child nodes (if the array were a binary tree)
    and find the largest value. If one of the children is larger swap the values and recurse into that subtree

    consider current index as largest
    """
    largest_index = i
    left_child = i * 2 + 1
    right_child = i * 2 + 2

    # compare with left child
    if left_child < n and arr[left_child] > arr[largest_index]:
        largest_index = left_child

    # compare with right child
    if right_child < n and arr[right_child] > arr[largest_index]:
        largest_index = right_child

    # if either of left / right child is the largest node
    if largest_index != i:
        arr[i], arr[largest_index] = arr[largest_index], arr[i]
        heapify(arr, n, largest_index)


def test_function(test_case):
    heapsort(test_case[0])
    if test_case[0] == test_case[1]:
        print("Pass")
    else:
        print("False")

arr = [3, 7, 4, 6, 1, 0, 9, 8, 9, 4, 3, 5]
solution = [0, 1, 3, 3, 4, 4, 5, 6, 7, 8, 9, 9]
test_case = [arr, solution]
test_function(test_case)


arr = [5, 5, 5, 3, 3, 3, 4, 4, 4, 4]
solution = [3, 3, 3, 4, 4, 4, 4, 5, 5, 5]
test_case = [arr, solution]
test_function(test_case)

arr = [99]
solution = [99]
test_case = [arr, solution]
test_function(test_case)


arr = [0, 1, 2, 5, 12, 21, 0]
solution = [0, 0, 1, 2, 5, 12, 21]
test_case = [arr, solution]
test_function(test_case)
