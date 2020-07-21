# Problem 2

This problem is implemented similarly to a normal binary search in an array, however it also compares the middle element 
to the first and the last element of the sequence, as is detailed in the code comments.

Being *N* the size of the input list, since half of the list is discarded at each iteration, at most log2(N) recursive
iterations are performed, and because we only store simple elements, it results in:

* Space and time complexity: O(log(N))  
