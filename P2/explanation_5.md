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

Through these iterations, it also checks if each character is already in the node's children or not. Since the children
element is a Python dictionary, I'm considering this check to be at constant time, according to this discussion:
https://knowledge.udacity.com/questions/282151    

* Time complexity: O(N)
* Space complexity: O(1)


## Suffixes method

The *suffixes* method of the *TrieNode* class recursively visits all children nodes below it exactly once and
concatenates the possible suffixes in a list, resulting in O(N) time complexity, considering *N* the total amount of
letters in the Trie (equals to the amount of nodes).

The concatenation of the found results in the major list takes O(k) time, k being the length of each result list.
In the end the sum of k will be equal to the number of final results, that is N.

* Time complexity: O(N)

As for the space complexity, we consider *N* to be the amount of complete words in the tree (or possible suffixes under
the given node, if it is not the root), and we allocate memory for each possible suffix, thus having:

* Space complexity: O(N)
