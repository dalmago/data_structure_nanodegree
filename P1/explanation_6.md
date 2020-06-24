# Problem 6

The provided `LinkedList` class for this problem was modified so we could keep a reference to the end of the linked
list, in order to add a new element in constant time.

Considering **N** to be the sum of the length of both linked lists:

For the `union` solution, a `set` was used to keep track of the elements already in the result list (in constant time),
thus avoiding having to traverse the linked list to remove duplicates. Since we only visit each element of the lists
once, its time complexity is O(N). As for the space, in the worst case scenario (all elements of both lists are
different) if will take up to N elements for the result linked list and N elements for the temporary `set`, so the space
complexity is also O(N).

Likewise, in the `intersection` solution, a set was used to keep track of the elements in constant time. All elements of
the first list were added to the set - O(1) - then the elements of the second list were checked. In the same way as
`union`, the time complexity for this solution is O(N). The space usage also grows linearly: the worst case scenario for
the intersection is when all elements are different within the list, but both lists have the same elements. In this
case, we would allocate N/2 elements in the result list, as well in both `sets`. In conclusion, the space complexity is
O(N).

* Time Complexity: O(N)
* Space Complexity: O(N)
