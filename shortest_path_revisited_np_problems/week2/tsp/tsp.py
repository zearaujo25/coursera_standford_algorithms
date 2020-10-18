def tsp(nodes):
    solution_array = {}
    destination = 1
    solution_array[destination] = create_base_case(nodes)
    for probleam_size in range(2,len(nodes)+1):
        print("problem size: {}".format(probleam_size))
        for bitmask in range(1,1<<probleam_size):
            for node in get_nodes(bitmask,exclude_node=1):
                previous_set = exclude_node_from_mask(bitmask,node)
                solution_array[bitmask,node] = min([solution_array[previous_set,previous_node] + get_distance(node,previous_node) for previous_node in get_nodes(previous_set,None)])
    return solution_array

def create_base_case(nodes):
    num_nodes = len(nodes)
    return {bitmask:float("inf") if bitmask !=1 else 0 for bitmask in range(1,1<<num_nodes )}


def get_nodes(bitmask,exclude_node=1):
    while bitmask:
        b = bitmask & (~bitmask+1)
        if b != exclude_node or exclude_node is None:
            yield b
        bitmask ^= b

def exclude_node_from_mask(bitmask,node): 
  
    # k must be greater than 0 
    if (node <= 0):  
        return bitmask 
    return (bitmask & ~(1 << (node - 1))) 

def get_distance(node1,node2):
    pass