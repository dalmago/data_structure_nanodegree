# Problem 5

## Insert method

The *insert* method of the *Trie* class is responsible for inserting each word into the Trie, this generating it. It
also calls the *insert* method of the *TrieNode* class, which has constant time and space complexity.
The worst case scenario would be if no word had any common prefix. As a consequence, being *N* the total amount of 
letters of all the words in the Trie, N nodes would be created. Also, N iterations would be performed since we have to 
iterate over all the letters.

* Time and space complexity: O(N)


## Find method

The *find* method of the *Trie* class finds and returns the node of a given prefix. Being *N* the length of the prefix,
*find* iterates N times and creates a constant amount of variables.

* Time complexity: O(N)
* Space complexity: O(1)


## Suffixes method

The *suffixes* method of the *TrieNode* class recursively visits all children nodes below it exactly once and
concatenates the the possible suffixes in a list, resulting in O(N) time complexity. Considering *N* the total amount of
letters in the Trie (equals to the amount of nodes):

* Time complexity: O(N)

As for the space complexity, we consider *N* to be the amount of complete words in the tree (or possible suffixes under
the given node, if it is not the root), and we allocate memory for each possible suffix, thus having:

* Space complexity: O(N)
