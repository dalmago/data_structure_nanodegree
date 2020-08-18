import heapq


def generate_graph(num_islands, bridge_config):
    graph = [list() for _ in range(num_islands)]  # empty list with num_islands sublists

    for isla1, isla2, cost in bridge_config:
        graph[isla1 - 1].append((isla2, cost))
        graph[isla2 - 1].append((isla1, cost))

    return graph

def get_minimum_cost_of_connecting(num_islands, bridge_config):
    """
    :param: num_islands - number of islands
    :param: bridge_config - bridge configuration as explained in the problem statement
    return: cost (int) minimum cost of connecting all islands
    TODO complete this method to return minimum cost of connecting all islands
    """

    # 1 - Create a graph with given number of islands, and the cost between each pair of islands
    graph = generate_graph(num_islands, bridge_config)  # adjacency matrix

    start_node = 1
    min_heap = [(0, start_node)]

    visited_islands = set()

    total_cost = 0

    while len(min_heap) > 0:
        current_cost, current_node = heapq.heappop(min_heap)

        if current_node not in visited_islands:
            visited_islands.add(current_node)
            total_cost += current_cost

        for destination, cost in graph[current_node - 1]:
            if destination not in visited_islands:
                heapq.heappush(min_heap, (cost, destination))

    return total_cost


def test_function(test_case):
    num_islands = test_case[0]
    bridge_config = test_case[1]
    solution = test_case[2]
    output = get_minimum_cost_of_connecting(num_islands, bridge_config)

    if output == solution:
        print("Pass")
    else:
        print("Fail")


num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
solution = 6
test_case = [num_islands, bridge_config, solution]
test_function(test_case)

num_islands = 5
bridge_config = [[1, 2, 5], [1, 3, 8], [2, 3, 9]]
solution = 13
test_case = [num_islands, bridge_config, solution]
test_function(test_case)

num_islands = 5
bridge_config = [[1, 2, 3], [1, 5, 9], [2, 3, 10], [4, 3, 9]]
solution = 31
test_case = [num_islands, bridge_config, solution]
test_function(test_case)
