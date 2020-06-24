# Problem 1

Considering **N** to be the initial capacity of the LRU cache:

To keep track of the least recently used elements, the chosen data structure was a doubly linked list. But since
traversing the list to find an element would take O(N) time, and our operations are required to take O(1), a second
data structure was used: a dictionary that maps the cache key to a node in the linked list.

This way, when `get(key)` is called, we can check if the key exists in our dictionary and, if it does, we have a direct
reference to its node in the list. All of this is run at constant time, thanks to dictionaries. Then we can get the
desired value and move the node to the end of the list, without having to traverse it to find which node to move. Since
we already have the tail reference, this also runs at constant time.

Furthermore, when `set(key, value)` is called, we check if the element already exists in the same way as `get` did. If
it exists, we get the reference to its node - time O(1) - and update the node's value. If the element does not exist in
our dictionary, we check if the cache has reached full capacity. If it has, the first element of our doubly linked list
is removed - time O(1) - and its key is removed from the dictionary - time O(1)). To conclude, a new node is created and
added to the end of the linked list and its reference is saved into the dictionary (both O(1) for time).

As for space, it grows linearly since for each cache element supported, we allocate a new node in the linked list and
also save its reference in a dictionary.

* Time Complexity: O(1)
* Space Complexity: O(N)
