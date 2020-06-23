# Problem 3

For the encoding part of the **Huffman Coding** algorithm, we first count the frequency each character occurs - O(n) -
and keep the result in a dictionary. Then the each character (and its frequency count) is inserted in a ordered linked
list (order by the frequency of each character). Since we must traverse the whole list to insert an element in order
(in the worst case scenario, we would always insert the larger element), the execution complexity is given by the sum
of an arithmetic progression with common difference 1 (first the list has 1 element, then 2, then 3, ... N-1, N):
(N^2 + N)/2. The same happens in the function called `huffman_reduce_list`, which takes the first two elements of the
list, combine them into one and re-insert into the list. The list has (N, N-1, N-2 ... 3, 2, 1) elements, also
represented by (N^2 + N)/2. Later in encoding process, each node of the tree is visited once again, creating a map for
each character and its respective Huffman code. Finally, each character is encoded. Therefore, the most significant
portion of the time complexity for the encoding function is the quadratic part: O(N^2).

As for the decoding section, we iterate over the bits of the encoded message, taking O(N) time, being N the size of the
encoded message.

In general:
* Complexity: O(N^2)
