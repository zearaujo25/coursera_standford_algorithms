from queue import Queue
def breadth_first_search(graph,node):
    node.mark_as_explored()
    node.set_distance(0)
    search_queue = Queue()
    search_queue.put(node)
    while not search_queue.empty():
        next_node = search_queue.get()
        for edge in graph.get_node_edges(next_node):
            destination = edge.get_destination(next_node)
            if not destination.is_explored():
                destination.mark_as_explored()
                destination.set_distance(next_node.get_distance() +1)
                search_queue.put(destination)

def find_connected_components(graph):
    number_of_conections = 0
    for node in graph.get_nodes():
        if not node.is_explored():
            number_of_conections+=1
            breadth_first_search(graph,node)
    return number_of_conections
