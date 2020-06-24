# Problem 4

Being **N** the sum of the number of users and groups in the structure, it doesn't matter how they're organized: 10E5
users in the main group would take the same amount the time to run as 10E5 minus 1 groups in a chain with one user in
the last subgroup. All the elements are visited exactly once (in the worst case scenario).

* Time Complexity: O(N)

If a user is not found in a group, but the group has subgroups, the `is_user_in_group` function will call itself
recursively passing the subgroups.

Call stack (suppose the user is not found):

- is_user_in_group('user', 'parent_group')
  - is_user_in_group('user', 'child_group')
    - is_user_in_group('user', 'grandchild_group')
      - ...

As for space complexity, the function `is_user_in_group` uses constant space: O(1). However, the implementation of
`Group` makes use of space linearly.

* Space Complexity: O(N)

For this problem, it would have been better if we used `sets` to hold the users instead of a `list`, so we could check
if the user exists in the current group at constant time. However, since we have to traverse the group list anyway, the
complexity would still be O(N). 
