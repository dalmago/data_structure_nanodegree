# Problem 4

In order to sort the list in a single traverse, two reference indexes are kept: one having the last position of the
zeros in the list and another having the first position of the twos in the list. As we traverse, if a zero is found it
is send to the beginning of the list, just after the last zero reference index. In a similar way, if a two is found, is
is send to the end of the list, just before the first two reference index. If a one is found, no action is taken.

When a zero is send to the beginning of the list, it is necessarily swapped with a one, since the element just after the
last zero index was already checked. So, in this case, we just swap the elements, increment the index and keep going.
However, when a two is send to the end of the list, there is no way to know which element it will swap with. So, after
the swap, the loop index is not incremented. This however does not disagree with the one traverse rule: the index is
not incremented (the same position is checked more than once) but the first two reference index is decremented, and
since it is the stop rule for the loop, exactly N comparisons will be made.

At the beginning of the function, a copy of the input list is made in order to return a different list, since lists are 
mutable in Python. This copy is not accounted in the space and time complexity, since it is not part of the sort
algorithm.

Considering *N* to be the length of the input list:

* Time complexity: O(N)
* Space complexity: O(1) - in-place sorting
