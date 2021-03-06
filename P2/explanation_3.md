# Problem 3

At first the input list of length *N* is sorted from larger to smaller elements using a merge sort algorithm, thus the
O(N log(N)) time complexity and O(N) space complexity.

After being sorted, the input values are used in pairs: one is added to the first number, and the other to the second
output number. This way the largest value in the sorted list will be the most significant digit of one number, the
second largest value will be the most significant digit of the other number, and so on. The larger the value is the
most significant position it will be in the output number. For this operation, the sorted list is traversed once (O(N))
and constant space is used.

Since N*log(N) takes longer then linear N:

* Time complexity: O(N log(N))
* Space complexity: O(N) 
