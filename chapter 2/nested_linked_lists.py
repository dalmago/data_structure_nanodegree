# Helper code

# A class behaves like a data-type, just like an int, float or any other built-in ones.
# User defined class
class Node:
    def __init__(self,
                 value):  # <-- For simple LinkedList, "value" argument will be an int, whereas, for NestedLinkedList, "value" will be a LinkedList
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


# User defined class
class LinkedList:
    def __init__(self, head):  # <-- Expects "head" to be a Node made up of an int or LinkedList
        self.head = head

    '''
    For creating a simple LinkedList, we will pass an integer as the "value" argument
    For creating a nested LinkedList, we will pass a LinkedList as the "value" argument
    '''

    def append(self, value):

        # If LinkedList is empty
        if self.head is None:
            self.head = Node(value)
            return

        # Create a temporary Node object
        node = self.head

        # Iterate till the end of the currrent LinkedList
        while node.next is not None:
            node = node.next

        # Append the newly creataed Node at the end of the currrent LinkedList
        node.next = Node(value)

    '''We will need this function to convert a LinkedList object into a Python list of integers'''

    def to_list(self):
        out = []  # <-- Declare a Python list
        node = self.head  # <-- Create a temporary Node object

        while node:  # <-- Iterate untill we have nodes available
            out.append(int(str(
                node.value)))  # <-- node.value is actually of type Node, therefore convert it into int before appending to the Python list
            node = node.next

        return out


def merge(list1, list2):
    # TODO: Implement this function so that it merges the two linked lists in a single, sorted linked list.
    '''
    The arguments list1, list2 must be of type LinkedList.
    The merge() function must return an instance of LinkedList.
    '''
    new_list = LinkedList(None)
    l1 = list1.head
    l2 = list2.head

    while l1 or l2:
        if l1 and l2:
            if l1.value < l2.value:
                new_list.append(l1.value)
                l1 = l1.next
            else:
                new_list.append(l2.value)
                l2 = l2.next
        elif l1:
            new_list.append(l1.value)
            l1 = l1.next
        elif l2:
            new_list.append(l2.value)
            l2 = l2.next

    return new_list


''' In a NESTED LinkedList object, each node will be a simple LinkedList in itself'''


class NestedLinkedList(LinkedList):
    def flatten(self):
        if self.head is None:
            return LinkedList(None)

        node = self.head
        merged_list = LinkedList(node.value.head)

        while node.next:
            merged_list = merge(merged_list, node.next.value)
            node = node.next

        return merged_list

# First Test scenario
''' Create a simple LinkedList'''
linked_list = LinkedList(Node(1)) # <-- Notice that we are passing a Node made up of an integer
linked_list.append(3) # <-- Notice that we are passing a numerical value as an argument in the append() function here
linked_list.append(5)

''' Create another simple LinkedList'''
second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

''' Create a NESTED LinkedList, where each node will be a simple LinkedList in itself'''
nested_linked_list = NestedLinkedList(Node(linked_list)) # <-- Notice that we are passing a Node made up of a simple LinkedList object
nested_linked_list.append(second_linked_list) # <-- Notice that we are passing a LinkedList object in the append() function here

print("testing")
solution = nested_linked_list.flatten() # <-- returns A LinkedList object
print(solution)
# expected_list = [1,2,3,4,5] # <-- Python list

# Convert the "solution" into a Python list and compare with another Python list
# assert solution.to_list() == expected_list, f"list contents: {solution.to_list()}"
print("end")
