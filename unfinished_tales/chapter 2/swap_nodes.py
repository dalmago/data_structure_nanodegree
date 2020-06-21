
class Node:
    """LinkedListNode class to be used for this problem"""
    def __init__(self, data):
        self.data = data
        self.next = None


"""
:param: head- head of input linked list
:param: `position_one` - indicates position (index) ONE
:param: `position_two` - indicates position (index) TWO
return: head of updated linked list with nodes swapped

TODO: complete this function and swap nodes present at position_one and position_two
Do not create a new linked list
"""


def swap_nodes(head, left_index, right_index):
    if head is None:
        return None

    node = head
    while left_index > 1:
        node = node.next

        left_index -= 1
        right_index -= 1

    # if left_index ends up as zero, the left_index is the head
    before_left = node

    while right_index > 1:
        node = node.next
        right_index -= 1

    before_right = node

    if left_index > 0:
        left_node_next = before_left.next.next
        before_left.next.next = before_right.next.next
    else:
        left_node_next = before_left.next
        before_left.next = before_right.next.next

    before_right.next.next = left_node_next

    if left_index > 0:
        before_left.next, before_right.next = before_right.next, before_left.next
    else:
        head = before_right.next
        before_left.next, before_right.next = before_right.next, before_left.next

    return head


def test_functions(test_case):
    head = test_case[0]
    left_index = test_case[1]
    right_index = test_case[2]

    left_node = None
    right_node = None

    temp = head
    index = 0
    try:
        while temp is not None:
            if index == left_index:
                left_node = temp
            if index == right_index:
                right_node = temp
                break
            index += 1
            temp = temp.next

        updated_head = swap_nodes(head, left_index, right_index)

        temp = updated_head
        index = 0
        pass_status = [False, False]

        while temp is not None:
            if index == left_index:
                pass_status[0] = temp is right_node
            if index == right_index:
                pass_status[1] = temp is left_node

            index += 1
            temp = temp.next

        if pass_status[0] and pass_status[1]:
            print("Pass")
        else:
            print("Fail")
        return updated_head
    except Exception as e:
        print("Fail")

# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()

arr = [3, 4, 5, 2, 6, 1, 9]
left_index = 2
right_index = 4
head = create_linked_list(arr)
test_case = [head, left_index, right_index]
updated_head = test_functions(test_case)
