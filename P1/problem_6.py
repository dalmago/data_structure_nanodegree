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

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def append_unique(self, value):
        # Same as the append above, but while traversing the list it also checks if the element already exists.
        # If it does, return without adding the element to the list.
        # This method takes advantage of the fact that, for a Linked List, we have to traverse it in order to add
        # an element to the end of the list.
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            if node.value == value:
                return
            node = node.next

        if node.value == value:
            return
        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def __contains__(self, item):
        # Helper method to check if item belongs to a LinkedList
        node = self.head
        while node:
            if node.value == item:
                return True
            node = node.next
        return False


def union(llist_1, llist_2):
    # Create new LinkedList for the answer
    new_list = LinkedList()

    # Traverse llist_1
    head1 = llist_1.head
    while head1:
        new_list.append_unique(head1.value)
        head1 = head1.next

    # Traverse llist_2
    head2 = llist_2.head
    while head2:
        new_list.append_unique(head2.value)
        head2 = head2.next

    return new_list


def intersection(llist_1, llist_2):
    # Creates a new Linked List for the answer
    new_list = LinkedList()

    # Traverse list 1
    head1 = llist_1.head
    while head1:
        if head1.value in llist_2:  # If element also in llist_2, append to the new_list
            new_list.append_unique(head1.value)
        head1 = head1.next

    return new_list


# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))
