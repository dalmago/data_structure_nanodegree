# Problem 4

Being **N** the sum of the number of users and groups in the structure, it doesn't matter how they're organized: 10E5
users in the main group would take the same amount the time to run as 10E5 minus 1 groups in a chain with one user in
the last subgroup. All the elements are visited exactly once (in the worst case scenario).

* Complexity: O(N)

For this problem, it would have been better if we used `sets` to hold the users instead of a `list`, so we could check
if the user exists in the current group at constant time. However, since we have to traverse the group list anyway, the
complexity would still be O(N). 
