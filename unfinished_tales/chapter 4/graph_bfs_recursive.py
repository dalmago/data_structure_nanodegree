from collections import deque

class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.children = []

    def add_child(self, new_node):
        self.children.append(new_node)

    def remove_child(self, del_node):
        if del_node in self.children:
            self.children.remove(del_node)

    def __repr__(self):
        return f"GraphNode({self.value})"


class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2)
            node2.add_child(node1)

    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_child(node2)
            node2.remove_child(node1)


def bfs_search(root_node, search_value):
    visited_nodes = set()
    visit_queue = deque()

    def bfs_recursive_helper(node, value):
        if node.value == value:
            return node

        visited_nodes.add(node)

        for child in node.children:
            if child not in visited_nodes and child not in visit_queue:
                visit_queue.append(child)

        if not visit_queue:
            return None

        return bfs_recursive_helper(visit_queue.popleft(), value)

    return bfs_recursive_helper(root_node, search_value)


nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')
nodeP = GraphNode('P')
nodeH = GraphNode('H')
nodeS = GraphNode('S')

graph1 = Graph([nodeS, nodeH, nodeG, nodeP, nodeR, nodeA] )
graph1.add_edge(nodeG, nodeR)
graph1.add_edge(nodeA, nodeR)
graph1.add_edge(nodeA, nodeG)
graph1.add_edge(nodeR, nodeP)
graph1.add_edge(nodeH, nodeG)
graph1.add_edge(nodeH, nodeP)
graph1.add_edge(nodeS, nodeR)


assert nodeA == bfs_search(nodeS, 'A')
assert nodeS == bfs_search(nodeP, 'S')
assert nodeR == bfs_search(nodeH, 'R')
