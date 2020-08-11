from random import randrange
from math import log,ceil
from copy import deepcopy


def find_min_cut(graph):
    trial_graph = deepcopy(graph)
    num_nodes = len(graph.get_nodes())
    while(num_nodes>2):
        edges = list(trial_graph.get_edges())
        edge_index = randrange(len(edges))
        choosen_edge = edges[edge_index] 
        trial_graph.contract(choosen_edge)
        num_nodes = len(trial_graph.get_nodes())
    return trial_graph

def random_contractions(graph):
    number_of_nodes = len(graph.get_nodes())
    number_of_trials = ceil(number_of_nodes**2)
    min_cut = None
    for i in range(0,number_of_trials):
        trial_min_cut = find_min_cut(graph)
        if min_cut is None:
            min_cut = trial_min_cut
        else:
            if(len(min_cut.get_edges()) > len(trial_min_cut.get_edges())):
                min_cut = trial_min_cut
    return min_cut