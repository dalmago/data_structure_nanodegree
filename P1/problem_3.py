# -*- coding: utf-8 -*-
# problem_3.py
# Author: Matheus Dal Mago
# 2020

import sys


class TreeNode:
    # Helper class to implement a node of the tree
    def __init__(self, freq, char=None):
        self.freq = freq
        self.char = char
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        if self.char:
            return f"TreeNode({self.char}: {self.freq})"
        return f"TreeNode({self.freq})"


class ListNode:
    # Helper class to implement a node of a linked list
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


def insert_ordered_node(head, tree_node):  # O(n), n being the number of elements already on the list
    # Helper function that inserts tree_node into the linked list head, ordering by tree_node.freq
    list_node = ListNode(tree_node)
    if head is None:  # First element in the list
        return list_node

    if list_node.value.freq <= head.value.freq:  # tree_node should become the head
        list_node.next = head
        return list_node

    node_before = head
    while node_before.next:  # Insert in ordered position
        if list_node.value.freq <= node_before.next.value.freq:  # found where to insert the new node
            break

        node_before = node_before.next

    list_node.next = node_before.next
    node_before.next = list_node
    return head


def huffman_reduce_list(head):
    # Helper function that takes the two elements that appear first in
    # the list and creates a new node with the sum of the frequencies

    if head is None:
        return None

    if head.next is None:
        return head

    # 3 - Pop-out two nodes with the minimum frequency
    first_element, second_element = head.value, head.next.value
    head = head.next.next  # Head after the popped-out nodes

    # 4 - Create new node with the sum of the frequencies
    new_tree_node = TreeNode(first_element.freq + second_element.freq)
    if first_element.freq <= second_element.freq:
        new_tree_node.left_child, new_tree_node.right_child = first_element, second_element
    else:
        new_tree_node.left_child, new_tree_node.right_child = second_element, first_element

    head = insert_ordered_node(head, new_tree_node)  # Insert newly created element back into the list

    # 5 - repeat until one element left
    return huffman_reduce_list(head)


def huffman_tree_map_leaves(tree_node, prefix, char_map):  # Visit each element of the tree exactly once
    # Takes a node from the tree, a prefix (that starts out as an empty string) and a char_map (empty dictionary),
    # traverse the tree concatenating 0 in the prefix for a left node and 1 for a right node. When a leaf is reached,
    # stores the character code (prefix) in the char_map.
    if tree_node.left_child is None and tree_node.right_child is None:
        if prefix == '':
            prefix = '0'
        char_map[tree_node.char] = prefix
        return

    huffman_tree_map_leaves(tree_node.left_child, prefix + "0", char_map)
    huffman_tree_map_leaves(tree_node.right_child, prefix + "1", char_map)


def huffman_encoding(data):
    # 1 - Count the frequency each char appears
    char_frequency = {}
    for char in data:  # O(n)
        if char in char_frequency:  # O(1)
            char_frequency[char] += 1  # O(1)
        else:
            char_frequency[char] = 1  # O(1)

    # 2 - Create a linked list ordered by the char frequency
    list_head = None
    for key, value in char_frequency.items():  # (N^2 + N) / 2
        tree_node = TreeNode(value, key)
        list_head = insert_ordered_node(list_head, tree_node)

    # 3, 4, 5 - Two nodes with minimum frequency become one
    list_head = huffman_reduce_list(list_head)  # (N^2 + N) / 2
    if list_head is None:
        return None, None

    tree_root = list_head.value

    # 6, 7 - generate a code for each character
    char_map = {}
    huffman_tree_map_leaves(tree_root, "", char_map)

    encoded_str = ""
    for char in data:  # O(N)
        encoded_str += char_map[char]

    return encoded_str, tree_root


def huffman_decoding(data, tree):
    # 1 - Starting out with an empty string
    decoded_str = ""

    tree_node = tree
    # 2 - Pick each bit from the encoded data
    for bit in data:
        # 3 - Traverse the tree
        if bit == '0':
            tree_node = tree_node.left_child
        else:
            tree_node = tree_node.right_child

        if tree_node is None:  # Special case when the tree has only the root node
            tree_node = tree

        if tree_node.left_child is None and tree_node.right_child is None:  # it is a leaf
            decoded_str += tree_node.char
            tree_node = tree  # back to the root of the tree

    return decoded_str


if __name__ == "__main__":
    count = 0

    # Test cases with empty strings, word with just one letter, word with the same letter repeatedly, words with all
    # letters different
    for sentences in ["The bird is the word", "", "arara", "b", "ccccccc", "0123456789"]:
        print("-------------------")
        print(f"Test case {count}:")
        print("The size of the data is: {}".format(sys.getsizeof(sentences)))
        print("The content of the data is: {}\n".format(sentences))

        encoded_data, tree = huffman_encoding(sentences)

        if encoded_data is not None and tree is not None:
            print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
            print("The content of the encoded data is: {}\n".format(encoded_data))

            decoded_data = huffman_decoding(encoded_data, tree)

            print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
            print("The content of the encoded data is: {}\n".format(decoded_data))

        else:
            print("Could not encode. String empty or has invalid characters.")

        count += 1
