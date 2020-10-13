from collections import deque
def bellman_shortest_path(graph,source):
    solution_array = deque()
    node_len = len(graph)
    create_base_cases(source, graph, solution_array)
    num_edges = 1 
    while num_edges < node_len:
        find_iteration_solution(graph, solution_array)
        #optimizing space by getting rid of unecessary solutions
        solution_array.popleft()
        num_edges+=1
    find_iteration_solution(graph,solution_array)
    return None if solution_array[-1] != solution_array[0] else solution_array[0]


def create_base_cases(source, graph, solution_array):
    base_case = {}
    base_case[source] = 0
    for node in graph.keys():
        if node != source:
            base_case[node] = float("inf")
    solution_array.append(base_case)
    

def find_iteration_solution(graph, solution_array):
    iteration_solution = {}
    for node in graph:
        min_path_next_node = min([ solution_array[-1][incoming_edge[0]] + incoming_edge[2] for incoming_edge in graph[node]['incoming_edges']]) if len(graph[node]['incoming_edges']) >0 else float("inf")
        iteration_solution[node] = min(min_path_next_node,solution_array[-1][node])
    solution_array.append(iteration_solution)
    


    

