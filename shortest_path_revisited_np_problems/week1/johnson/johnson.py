from collections import deque
from bellman_ford import bellman_shortest_path
from dijkstra_custom_heap import dijkstra_custom_heap
from copy import deepcopy

def johnson_shortest_path(graph):
    aux_graph = create_extra_node_graph(graph)
    node_weights = bellman_shortest_path(aux_graph,0)
    if node_weights is None:
        return None
    graph = reweight_graph(aux_graph,node_weights)
    weighted_shortest_paths = find_shortest_paths(graph)
    final_shortest_path = weight_back(weighted_shortest_paths,node_weights)
    return final_shortest_path

def create_extra_node_graph(graph):
    aux_graph = deepcopy(graph)
    extra_node_edges = {'incoming_edges':set(),'leaving_edges':set()}
    for node in graph:
        extra_node_edges['leaving_edges'].add((0,node,0))
        aux_graph[node]['incoming_edges'].add((0,node,0))
    aux_graph[0] = extra_node_edges
    return aux_graph

def reweight_graph(graph,node_weights):
    new_graph = {}

    for node in graph: 
        new_graph[node] = {'leaving_edges':set(),'incoming_edges':set()}
        for edge in graph[node]['leaving_edges']:
            new_edge_weight = edge[2] + node_weights[edge[0]] - node_weights[edge[1]]
            new_edge = (edge[0],edge[1],new_edge_weight)
            new_graph[node]['leaving_edges'].add(new_edge)

        for edge in graph[node]['incoming_edges']:
            new_edge_weight = edge[2] + node_weights[edge[0]] - node_weights[edge[1]]
            new_edge = (edge[0],edge[1],new_edge_weight)
            new_graph[node]['incoming_edges'].add(new_edge)
    return new_graph

def find_shortest_paths(graph):
    node_paths = {}
    for node in graph:
        dijkstra_result = dijkstra_custom_heap(graph,node)
        node_paths[node] = dijkstra_result
    return node_paths

def weight_back(weighted_shortest_paths,node_weights):
    true_shortest_path = {}
    for source_node in weighted_shortest_paths:
        true_shortest_path[source_node] = {}
        for destination_node in weighted_shortest_paths[source_node]:
            true_shortest_path[source_node][destination_node] =  weighted_shortest_paths[source_node][destination_node] - node_weights[source_node] + node_weights[destination_node]
    return true_shortest_path
