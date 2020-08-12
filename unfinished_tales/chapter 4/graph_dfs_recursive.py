# Class Node representation.
class Node:
    def __init__(self, val):
        self.value = val
        self.children = []

    def add_child(self, new_node):
        self.children.append(new_node)

    def remove_child(self, del_node):
        if del_node in self.children:
            self.children.remove(del_node)

    def __repr__(self):
        return f"Node({self.value})"


class Graph():
    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1, node2):
        if (node1 in self.nodes and node2 in self.nodes):
            node1.add_child(node2)
            node2.add_child(node1)

    def remove_edge(self, node1, node2):
        if (node1 in self.nodes and node2 in self.nodes):
            node1.remove_child(node2)
            node2.remove_child(node1)


def dfs_recursion_start(start_node, search_value):
    visited_set = {start_node}

    def dfs_recursive_helper(node, search_value):
        if node.value == search_value:
            return node

        for child_node in node.children:
            if child_node not in visited_set:
                visited_set.add(child_node)
                child_search = dfs_recursive_helper(child_node, search_value)
                if child_search:
                    return child_search

        return None

    return dfs_recursive_helper(start_node, search_value)


# Creating a graph as above.
nodeG = Node('G')
nodeR = Node('R')
nodeA = Node('A')
nodeP = Node('P')
nodeH = Node('H')
nodeS = Node('S')

graph1 = Graph([nodeS,nodeH,nodeG,nodeP,nodeR,nodeA] )

graph1.add_edge(nodeG,nodeR)
graph1.add_edge(nodeA,nodeR)
graph1.add_edge(nodeA,nodeG)
graph1.add_edge(nodeR,nodeP)
graph1.add_edge(nodeH,nodeG)
graph1.add_edge(nodeH,nodeP)
graph1.add_edge(nodeS,nodeR)

# To verify that the graph is created accurately.
# Let's just print all the parent nodes and child nodes.
for each in graph1.nodes:
    print('parent node = ',each.value,end='\nchildren\n')
    for each in each.children:
        print(each.value,end=' ')
    print('\n')


assert nodeA == dfs_recursion_start(nodeG, 'A')
assert nodeA == dfs_recursion_start(nodeS, 'A')
assert nodeS == dfs_recursion_start(nodeP, 'S')
assert nodeR == dfs_recursion_start(nodeH, 'R')
