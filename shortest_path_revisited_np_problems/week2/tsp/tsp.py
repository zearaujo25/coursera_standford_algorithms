from math import sqrt,log2
def tsp(nodes):
    solution_array =  create_base_case(nodes)
    for probleam_size in range(2,len(nodes)+1):
        for bitmask in generate_bitmask(probleam_size):
            #Iterando sobre todos os nos excluindo o primeiro
            for destination_node in get_nodes(bitmask,excluded_node=1):
                solution_array[bitmask][destination_node] = {}
                previous_set = exclude_node_from_mask(bitmask,destination_node)
                iteration_possibilities = create_iteration_possibilities(nodes, solution_array, destination_node, previous_set)
                solution_array[bitmask][destination_node] = min(iteration_possibilities)

    return get_final_answer(solution_array[(1<<len(nodes))-1],nodes)

def create_iteration_possibilities(nodes, solution_array, node, previous_set):
    possibilities = []
    for previous_node in get_nodes(previous_set,None):
        solution = solution_array[previous_set][previous_node] + get_distance(nodes[node],nodes[previous_node])
        possibilities.append(solution)
    return possibilities

def create_base_case(nodes):
    solution_array = {}
    num_nodes = len(nodes)
    for bitmask in range(1,(1<<num_nodes)-1 ):
        #Sempre precisamos incluir o primeiro no. por isso fazemos um or para garatir que as mascaras sempre o possuem
        solution_array[bitmask|1] = {1:float("inf") if bitmask !=1 else 0 }
    return solution_array

def generate_bitmask(probleam_size):
    for bitmask in range(1,(1<<probleam_size)-1):
        yield bitmask | 1


def get_nodes(bitmask,excluded_node=1):
    while bitmask:
        b = bitmask & (~bitmask+1)
        if b != excluded_node or excluded_node is None:
            #retornando a posicao no bit 
            yield int(log2(b) + 1)
        bitmask ^= b

def exclude_node_from_mask(bitmask,node): 
    # node must be greater than 0 
    if (node <= 0):  
        return bitmask 
    return (bitmask & ~(1 << (node - 1))) 

def get_distance(node1,node2):
    return sqrt((node1[0]-node2[0])**2 + (node1[1]-node2[1])**2 )

def get_final_answer(solutions,nodes):
    return min([solutions[destination] + get_distance(nodes[1],nodes[destination]) if destination !=1 else float("inf") for destination in solutions])