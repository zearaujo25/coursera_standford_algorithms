def wis(weighted_nodes):
    solution_array = []
    solution_array.append(0)
    solution_array.append(weighted_nodes[0])
    for i,node_weight in enumerate(weighted_nodes[1:]):
        solution_array.append(max(solution_array[i+1],solution_array[i]+node_weight))
    
    solution_nodes = set()
    i = len(solution_array) -1
    while i>=1:
        if solution_array[i-1] >=solution_array[i-2] + weighted_nodes[i-1]:
            i+=-1
        else:
            solution_nodes.add(i-1)
            i+=-2
    
    return solution_nodes