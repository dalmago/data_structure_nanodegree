# -*- coding: utf-8 -*-
# problem_6.py
# Author: Matheus Dal Mago
# 2020


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        cur_head = self.head
        if cur_head is None:
            return "<empty>"
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value)
            if cur_head.next:
                out_string += " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        # Append using tail reference, taking constant time
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return

        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node


def union(llist_1, llist_2):
    # Create new LinkedList for the answer
    new_list = LinkedList()

    # Set to keep track of which elements are already in the new list
    union_set = set()

    # Traverse llist_1
    head1 = llist_1.head
    while head1:
        if head1.value not in union_set:  # O(1)
            new_list.append(head1.value)  # O(1)
            union_set.add(head1.value)  # O(1)

        head1 = head1.next

    # Traverse llist_2
    head2 = llist_2.head
    while head2:
        if head2.value not in union_set:
            new_list.append(head2.value)
            union_set.add(head2.value)

        head2 = head2.next

    return new_list


def intersection(llist_1, llist_2):
    # Creates a new Linked List for the answer
    new_list = LinkedList()

    # Creates a helper set that will be used to identify which element belongs to both the lists
    list1_set = set()

    # Traverse list 1 and add all elements to the set
    head1 = llist_1.head
    while head1:
        list1_set.add(head1.value)  # O(1)
        head1 = head1.next

    # Helper set that keeps elements added to the new_list, to avoid duplicates
    new_list_set = set()

    # Traverse list 2
    head2 = llist_2.head
    while head2:
        if head2.value in list1_set:  # If element of llist_2 also in llist_1, append to the new_list
            if head2.value not in new_list_set:  # Avoid duplicates - O(1)
                new_list.append(head2.value)
                new_list_set.add(head2.value)
        head2 = head2.next

    return new_list


if __name__ == "__main__":
    # Test case 1
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2))  # 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11
    print(intersection(linked_list_1, linked_list_2))  # 6 -> 4 -> 21

    # Test case 2
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print(union(linked_list_3, linked_list_4))  # 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21
    print(intersection(linked_list_3, linked_list_4))  # <empty>

    # Test case 3
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [1]
    element_2 = []

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print(union(linked_list_3, linked_list_4))  # 1
    print(intersection(linked_list_3, linked_list_4))  # <empty>

    # Test case 4
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = []
    element_2 = []

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print(union(linked_list_3, linked_list_4))  # <empty>
    print(intersection(linked_list_3, linked_list_4))  # <empty>

    # Test case 5
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [2]
    element_2 = [2]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print(union(linked_list_3, linked_list_4))  # 2
    print(intersection(linked_list_3, linked_list_4))  # 2

    # Test case 6
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [6, 6, 6, 6, 6, 6]
    element_2 = [6, 6, 6, 6, 6]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print(union(linked_list_3, linked_list_4))  # 6
    print(intersection(linked_list_3, linked_list_4))  # 6

    # Test case 7
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [7, 7, 7, 7, 7]
    element_2 = [1, 2, 3, 4, 5, 6]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print(union(linked_list_3, linked_list_4))  # 7 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
    print(intersection(linked_list_3, linked_list_4))  # <empty>

