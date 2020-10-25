from math import sqrt,log2
from copy import deepcopy
def tsp(nodes):
    visited_nodes, not_visited_nodes, current_node,tour_distance = set_initial_state(nodes)
    while len(visited_nodes) != len(nodes):
        next_node = None
        next_node_distance = float("inf")
        next_node_distance, next_node = find_next_node(not_visited_nodes, nodes, current_node, next_node_distance, next_node)
        tour_distance += next_node_distance
        visited_nodes.add(next_node)
        not_visited_nodes.remove(next_node)
        current_node = next_node    
    return tour_distance + get_distance(nodes[1],nodes[current_node]) 

def set_initial_state(nodes):
    not_visited_nodes = set(nodes.keys())
    visited_nodes = set()
    visited_nodes.add(1)
    not_visited_nodes.remove(1)
    current_node = 1
    tour_distance = 0
    return visited_nodes, not_visited_nodes, current_node,tour_distance

def find_next_node(not_visited_nodes, nodes, current_node, next_node_distance, next_node):
    for candidate_node in not_visited_nodes:
        candidate_node_distance = get_distance(nodes[current_node],nodes[candidate_node])
        if candidate_node_distance <= next_node_distance:
            if candidate_node_distance == next_node_distance:
                next_node_distance = candidate_node_distance if candidate_node < next_node else next_node_distance
                next_node = candidate_node if candidate_node < next_node else next_node
    return next_node_distance, next_node

def get_distance(node1,node2):
    return sqrt((node1[0]-node2[0])**2 + (node1[1]-node2[1])**2 )