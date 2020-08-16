from queue import LifoQueue
def depth_first_search(graph,start_node):
    start_node.mark_as_explored()
    search_stack = LifoQueue()
    search_stack.put(start_node)
    while not search_stack.empty():
        next_node = search_stack.get()
        for edge in graph.get_node_edges(next_node):
            destination = edge.get_destination(next_node)
            if not destination.is_explored():
                destination.mark_as_explored()
                search_stack.put(destination)

def depth_first_search_recursive(graph,start_node,current_label=None):
    start_node.mark_as_explored()
    for edge in graph.get_node_edges(start_node):
        destination = edge.get_destination(start_node)
        current_label = depth_first_search_recursive(graph,destination,current_label)
    start_node.set_distance(current_label)
    return current_label-1 if current_label is not None else None
    
def topological_sort(graph):
    nodes = graph.get_nodes()
    current_label = len(nodes)
    for node in nodes:
        if not node.is_explored():
            depth_first_search_recursive(graph,node,current_label)
    pass


def find_strongly_connected_components(graph):
    pass
