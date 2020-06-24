# Problem 3

Considering **N* to be the length of the string being encoded/decoded:

For the encoding part of the **Huffman Coding** algorithm, we first count the frequency each character occurs - time
O(n) - and keep the result in a dictionary. Then the each character (and its frequency count) is inserted in a ordered
linked list (order by the frequency of each character). Since we must traverse the whole list to insert an element in
order (in the worst case scenario, we would always insert the largest element), the time complexity is given by the sum
of an arithmetic progression with common difference 1 (first the list has 1 element, then 2, then 3, ... N-1, N):
(N^2 + N)/2. The same happens in the function called `huffman_reduce_list`, which takes the first two elements of the
list, combine them into one and re-insert into the list. The list has (N, N-1, N-2 ... 3, 2, 1) elements, also
represented by (N^2 + N)/2. Later in encoding process, each node of the tree is visited once again, creating a map for
each character and its respective Huffman code. Finally, each character is encoded. Therefore, the most significant
portion of the time complexity for the encoding function is the quadratic part: O(N^2).
For the space complexity, we initially store up to N positions in a dictionary to keep count of each character frequency
(worst case scenario when all characters are different). Then a linked list that grows up to N elements is created.
When building the `Huffman Tree`, up to 2*N nodes could be created in the worst case scenario. Finally, a map of each
character's code is created, but it also grows linearly, making the space complexity O(N).

As for the decoding section, we iterate over the bits of the encoded message, taking O(N) time. The only space used then
is the decoded message itself, that has size N.

In general:
* Time Complexity: O(N^2)
* Space Complexity: O(N)

Recursion:

`huffman_reduce_list` is a helper function that takes the first and second element of a linked list, combines them and
add the combined node back to the list (in the right position). The recursion stops when there is only one element left
on the list. Its call stack could be represented by:
- huffman_reduce_list([1, 2, 4, 6, 8])
  - 1 + 2 = 3
  - huffman_reduce_list([3, 4, 6, 8])
    - 3 + 4 = 7
    - huffman_reduce_list([6, 7, 8])
      - 6 + 7 = 13
      - huffman_reduce_list([8, 13])
        - 8 + 13 = 21
        - huffman_reduce_list([21])
          - returns

`huffman_tree_map_leaves` is another helper function used to build a map of the Huffman code of each leave of the tree.
If a node is a leaf, it stores the code in the map and return. If it's not, it changes the prefix (append '0' for the
left child and '1' for the right child) and call itself recursively for each child.
- huffman_tree_map_leaves(root, '', {})  # initially an empty prefix and empty map
  - huffman_tree_map_leaves(left_child, '0', {})
    - huffman_tree_map_leaves(left_left_child, '00', {})
      - it is a leaf! add '00' to the map
    - huffman_tree_map_leaves(left_right_child, '01', {00})
      - it is a leaf! add '01' to the map
  - huffman_tree_map_leaves(right_child, '1', {'00', '01'})
    - it is a leaf! add '1' to the map
