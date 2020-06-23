# -*- coding: utf-8 -*-
# problem_1.py
# Author: Matheus Dal Mago
# 2020


# All operations must take O(1) time.

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

    def __repr__(self):
        # Helper function for debugging
        return f"Node({self.key}: {self.value})"


class LRU_Cache:
    def __init__(self, capacity):
        # Initialize class variables
        self.remaining_capacity = capacity

        self.list_head = None
        self.list_tail = None
        self.nodes_reference = {}  # Empty dictionary

    def _move_node_to_tail(self, node):
        # Helper function that moves node to the tail of the double linked list.

        # Point node's previous.next reference
        if node.previous:
            node.previous.next = node.next
        else:  # node is the head of the list
            self.list_head = node.next

        # Point node's next.previous reference
        if node.next:
            node.next.previous = node.previous
        else:
            self.list_tail = node.previous
            # We are setting self.list_tail in multiple occasions.
            # This code could be optimized, but it is easier to understand this way.

        # Move node to the tail
        if self.list_tail:
            self.list_tail.next = node
            node.previous = self.list_tail
        else:
            self.list_head = node

        self.list_tail = node
        node.next = None
        # else: node is already the tail

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.nodes_reference:  # cache hit
            node = self.nodes_reference[key]  # get the reference to the node
            self._move_node_to_tail(node)
            return node.value
        return -1  # miss

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at full capacity, remove the oldest item
        if key in self.nodes_reference:
            node = self.nodes_reference[key]  # Get node reference
            node.value = value  # Update node's value
            self._move_node_to_tail(node)

        else:
            # Insert new node
            if self.remaining_capacity <= 0:  # Cache is full
                if self.list_head is None:
                    return
                lru_node = self.list_head  # Get LRU element
                self.list_head = lru_node.next  # Remove from double linked list
                if self.list_head:
                    self.list_head.previous = None
                else:  # All elements removed
                    self.list_tail = None

                del self.nodes_reference[lru_node.key]  # Delete from the reference's dictionary

            else:
                self.remaining_capacity -= 1

            node = Node(key, value)  # Create new node
            self.nodes_reference[key] = node  # Update the node reference dictionary

            # Add to the tail
            node.previous = self.list_tail
            if self.list_head is None:  # Only element in the list
                self.list_head = node
            else:
                self.list_tail.next = node

            self.list_tail = node


if __name__ == "__main__":
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    print(our_cache.get(1))  # returns 1
    print(our_cache.get(2))  # returns 2
    print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    print(our_cache.get(3))  # returns -1 because the cache reached its capacity and 3 was the least recently used entry

    my_cache = LRU_Cache(0)
    my_cache.set(1, 1)
    my_cache.set(2, 2)
    my_cache.set(3, 3)
    print(my_cache.get(1))  # returns -1 because the cache has size 0
    print(my_cache.get(2))  # returns -1 because the cache has size 0
    print(my_cache.get(3))  # returns -1 because the cache has size 0

    their_cache = LRU_Cache(-1)  # negative size, should never set any element
    their_cache.set(1, 1)
    print(their_cache.get(2))  # returns -1

    your_cache = LRU_Cache(1)
    your_cache.set("a", "first letter")
    your_cache.set("c", "third letter")
    your_cache.set("b", "second letter")

    print(your_cache.get("a"))  # returns -1 because 'a' was already removed from the cache
    print(your_cache.get("b"))  # returns 'second letter'
    print(your_cache.get("c"))  # returns -1
