from queue import Queue
def breadth_first_search(graph,node):
    node.mark_as_explored()
    search_queue = Queue()
    search_queue.put(node)
    while not search_queue.empty():
        next_node = search_queue.get()
        for edge in graph.get_node_edges(next_node):
            destination = edge.get_destination(next_node)
            if not destination.is_explored():
                destination.mark_as_explored()
                search_queue.put(destination)

