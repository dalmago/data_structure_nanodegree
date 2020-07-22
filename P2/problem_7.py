# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(root_handler)

    def insert(self, path_list, handler):
        # Similar to our previous example you will want to add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        my_node = self.root

        for path in path_list:
            my_node = my_node.insert(path)  # .insert method already checks if path already exist

        my_node.handler = handler

    def find(self, path_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        my_node = self.root

        for path in path_list:
            if path not in my_node.children:
                return None
            my_node = my_node.children[path]

        return my_node.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, path):
        # Insert the node as before
        if path not in self.children:
            self.children[path] = RouteTrieNode()

        # returns the just added node
        return self.children[path]

    def __repr__(self):
        # Helper function to help while debugging
        return f"{self.handler if self.handler else ''}-{', '.join(self.children.keys())}"


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(root_handler)
        self.handler_404 = not_found_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        split_path = self.split_path(path)
        self.route_trie.insert(split_path, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        split_path = self.split_path(path)
        route_trie_handler = self.route_trie.find(split_path)

        if not route_trie_handler:  # not found
            return self.handler_404
        return route_trie_handler

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        path = path.strip("/")  # O(N) - remove trailing slashes
        if not path:
            return []

        return path.split('/')  # O(N)


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/abouts/", "abouts tricky handler")

# # some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler'
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler'
print(router.lookup("/home/about/me"))  # should print 'not found handler'
print(router.lookup("/abouts/"))  # should print 'abouts tricky handler'
print(router.lookup("/home/abouts/"))  # should print 'not found handler'
print(router.lookup("/abouts/you"))  # should print 'not found handler'
