# Problem 6

The provided `LinkedList` class for this problem was modified so we could keep a reference to the end of the linked
list, in order to add a new element in constant time.

For the `union` solution, a `set` was used to keep track of the elements already in the result list (in constant time),
thus avoiding having to traverse the linked list to remove duplicates. Since we only visit each element of the lists
once, its complexity is O(n).

Likewise, in the `intersection` solution, a set was used to keep track of the elements in constant time. All elements of
the first list were added to the set - O(1) - then the elements of the second list were checked. In the same way as
`union`, the complexity for this solution is O(n).

* Complexity: O(N)
