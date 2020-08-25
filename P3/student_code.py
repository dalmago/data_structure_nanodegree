import math
import heapq

# Computes the Euclidean distance between two points
def nodes_distance(node1, node2):
    # Each point must have the coordinates [x, y]
    return math.sqrt((node1[0] - node2[0]) ** 2 + (node1[1] - node2[1]) ** 2)


def shortest_path(M, start, goal):
    print("shortest path called")

    # Set of already explored nodes
    explored_nodes = set()

    # Being g = current path cost from start and h = estimated distance to goal:
    element = [nodes_distance(M.intersections[start], M.intersections[goal]), 0, [start]]  # [g + h, g, node list from start]
    frontier = [element]  # priority queue
    frontier_dict = {start: element}  # dictionary that points to the same reference than items in the priority queue

    # Dictionary that keeps a node's estimate distance to the goal, to avoid calculating the same value more than once
    estimated_goal_distance = {}

    while frontier:
        dist, path_cost, node_list = heapq.heappop(frontier)  # get node in the frontier with smallest g + h so far
        current_node = node_list[-1]

        # remove node from frontier dict and add to explored set
        del frontier_dict[current_node]
        explored_nodes.add(current_node)

        if current_node == goal:  # the goal node is being explored
            return node_list

        for road_to in M.roads[current_node]:  # iterate over roads
            if road_to in explored_nodes:
                continue

            # Get node's estimate to goal
            node_estimate_to_goal = estimated_goal_distance.get(road_to, None)
            if node_estimate_to_goal is None:  # if it has not been calculated before
                estimated_goal_distance[road_to] = nodes_distance(M.intersections[road_to], M.intersections[goal])
                node_estimate_to_goal = estimated_goal_distance[road_to]

            # Get node's real path cost so far
            # No need to store this result for later, the same combination will never be calculated twice
            node_path_cost = path_cost + nodes_distance(M.intersections[current_node], M.intersections[road_to])

            # Add node to the list representing the path so far
            node_path = node_list.copy()
            node_path.append(road_to)

            if road_to in frontier_dict:
                if node_path_cost + node_estimate_to_goal < frontier_dict[road_to][0]:  # only updates if found value is smaller
                    # update values in priority queue
                    frontier_dict[road_to][0] = node_path_cost + node_estimate_to_goal
                    frontier_dict[road_to][1] = node_path_cost
                    frontier_dict[road_to][2] = node_path
                    heapq.heapify(frontier)

            else:
                # add intersection to frontier
                element = [node_path_cost + node_estimate_to_goal, node_path_cost, node_path]
                heapq.heappush(frontier, element)
                frontier_dict[road_to] = element

    return None
