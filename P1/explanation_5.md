# Problem 5

The BlockChain was implemented using a linked list, where each node of the list is a Block. Since we always add elements
to the end of the list, a reference to the tail is kept, making insertion time constant. On the other hand, the linked
list grows linearly as we add more transactions. Considering **N** to be the number of transactions made:

* Time Complexity: O(1)
* Space Complexity: O(N)
