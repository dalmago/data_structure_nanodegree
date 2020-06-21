# Problem 2

Considering **N** to be the number of directories and files in the `path` input and its sub-directories, without caring
 about the way it is organized (since we are going to visit all the elements once, regardless of they being files or
 folders, it doesn't matter if we have 5 files in the root dir or if we have 4 folders, one inside of the other, and a
 file in the fifth level), and `k` to be a constant symbolizing the time it takes to verify if a specific path is a
 directory or a file, and to list its content, we can say that:

 * T(n) = T(n-1) + k
 *  T(n-1) = T(n-2) + k
 * ...
 * T(1) = k
 * T(n) = k.n


* Time complexity: O(N)

This problem could be solved without implementing a helper function: `find_files` could call itself recursively, but
by doing so, it would have to return a list. This way, the recursive function that called itself would have to traverse 
that returned list and concatenate all elements to a list it created. This would generate more complexity to the code,
since aside from checking each node (file or folder), each call would have to concatenate every result found.

Creating a helper function avoids this problem, because each call can concatenate the results found to the same list,
that is created only once.
