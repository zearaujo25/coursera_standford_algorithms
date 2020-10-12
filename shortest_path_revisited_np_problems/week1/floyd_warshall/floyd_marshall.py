from collections import deque
def floyd_marshall_all_shortest_paths(graph):
    solution_array = deque()
    create_base_cases(graph,solution_array)
    for node_k in graph:
        process_iteration(graph, solution_array, node_k)
        #cleaning not used solutions
        solution_array.popleft()
    if has_negative_cylce(solution_array):
        return None
    else:
        return solution_array[0]

def create_base_cases(graph,solution_array):
    i_iteration = {}
    for node_i in graph:
        i_iteration[node_i] = {}
        for node_j in graph:            
            i_j_edges = [edge[2] for edge in graph[node_i]["outgoing_edges"] if edge[1] == node_j]
            min_edge  = min(i_j_edges) if len(i_j_edges) > 0 else None
            i_iteration[node_i][node_j] = min_edge if min_edge is not None else float("inf")
            if node_i == node_j:
                i_iteration[node_i][node_j] = min((0,i_iteration[node_i][node_j]))
    
    solution_array.append(i_iteration)

def process_iteration(graph, solution_array, node_k):
    i_iteration = {}
    for node_i in graph:
        i_iteration[node_i] = {}
        for node_j in graph:
            i_iteration[node_i][node_j] = min((solution_array[-1][node_i][node_j],solution_array[-1][node_i][node_k] + solution_array[-1][node_k][node_j]))
    solution_array.append(i_iteration)

def has_negative_cylce(solution_array):
    for node in solution_array[0]:
        if solution_array[0][node][node] < 0:
            return True
    return False