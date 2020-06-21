class BinaryTreeNode:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __repr__(self):
        return f'BST Node({self.data})'

def diameter_of_binary_tree(root):
    """
    :param: root - Root of binary tree
    TODO: Complete this method and return diameter (int) of binary tree
    """

    def diameter_recursive_helper(node):
        if node is None:
            return 0, 0

        left_sub = diameter_recursive_helper(node.left)
        right_sub = diameter_recursive_helper(node.right)

        major_diam = left_sub[0] + right_sub[0]

        return (1 + max(left_sub[0], right_sub[0]), max(major_diam, left_sub[1], right_sub[1]))

    return max(diameter_recursive_helper(root))


from queue import Queue


def convert_arr_to_binary_tree(arr):
    """
    Takes arr representing level-order traversal of Binary Tree
    """
    index = 0
    length = len(arr)

    if length <= 0 or arr[0] == -1:
        return None

    root = BinaryTreeNode(arr[index])
    index += 1
    queue = Queue()
    queue.put(root)

    while not queue.empty():
        current_node = queue.get()
        left_child = arr[index]
        index += 1

        if left_child is not None:
            left_node = BinaryTreeNode(left_child)
            current_node.left = left_node
            queue.put(left_node)

        right_child = arr[index]
        index += 1

        if right_child is not None:
            right_node = BinaryTreeNode(right_child)
            current_node.right = right_node
            queue.put(right_node)
    return root

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    root = convert_arr_to_binary_tree(arr)
    output = diameter_of_binary_tree(root)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arr = [1, 2, 3, 4, 5, None, None, None, None, None, None]
solution = 3
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 3, 4, None, 5, None, None, None, None, None]
solution = 4
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 3, None, None, 4, 5, 6, None, 7, 8, 9, 10, None, None, None, None, None, None, 11, None, None, None]
solution = 6
test_case = [arr, solution]
test_function(test_case)
