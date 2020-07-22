# Problem 7

## Add handler
The *add_handler* method first split the path into a list (iterates over each letter of the path). It then calls the
*insert* method of the *RouterTrie* class, that iterates over the nodes if they already exist or create new ones (adding
a new node takes constant time since we insert it into a Python dictionary). The number of nodes is proportional to the
sections of the given path, however since we have to iterate over each letter to find the slashes (and also store the
whole string), we are considering *N* to be the length of the path:

* Time and space complexity: O(N)


## Lookup
The *lookup* method also iterates over the nodes trying to find out if the given path exists in the Trie, however as
in the add handler method, we also have to iterate over each letter of the path, which is more significant than
iterating over the nodes. So, *N* being the length of the path:

* Time complexity: O(N)

Since we just store temporary variables to try to find the handler of the given path:

* Space complexity: O(1)
