
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_linked_list(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head


def even_after_odd(head):
    """
    :param - head - head of linked list
    return - updated list with all even elements are odd elements
    """
    if not head.next:
        return head

    new_head = head
    before_head = None
    while head.next:
        node_ref = head
        if head.data % 2 == 0:  # even number
            while node_ref.next and node_ref.next.data % 2 == 0:  # search for odd number
                node_ref = node_ref.next

            if node_ref.next:  # found
                odd_node = node_ref.next
                node_ref.next = odd_node.next

                if new_head == head:
                    new_head = odd_node
                    odd_node.next = head

                else:
                    odd_node.next = head
                    before_head.next = odd_node
                    # head = before_head  # keep the head in the same place

                head = odd_node

            else:
                break

        before_head = head
        head = head.next

    return new_head


my_list = create_linked_list([2,4,6,8,1,3,5,7])
x = even_after_odd(my_list)
