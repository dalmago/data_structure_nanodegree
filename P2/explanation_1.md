# Problem 1

Considering *N* to be the input value, the algorithm tries to find its square root by looking from 0 to N (N is included
because the numbers 0 and 1 are the square root of themselves) in a binary search. It tests the square of the middle 
element and, if it is not the floored square root of N, discards half of the elements and keeps searching recursively on 
the other half.

In the worst case scenario, we will have log2(N) calls to the recursive function, that other from the recursion only
has simple statement, thus having:

* Space and time complexity: O(log(N)) 
