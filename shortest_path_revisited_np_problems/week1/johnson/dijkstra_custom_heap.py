from heap import Heap

def dijkstra_custom_heap(graph,s):
    distances = {}
    distances[s] = 0
    heap = Heap(heap_type='min')
    update_heap(graph, s, distances, heap)
    while len(distances) != len(graph):
            node_weight_visited = visit_next_node(distances,graph,heap)
            if node_weight_visited is None:
                #no reachable node
                break
    return distances

def update_heap(graph, next_node, distances, heap):
    for edge in graph[next_node]['leaving_edges']:
        node = edge[0]
        weight = edge[1]
        node_score = distances[next_node] +weight
        new_score_node = (node,node_score)
        if node in distances:
            continue
        if node in heap.position_map:
            #update heap
            element_in_heap = heap.get_node_element(node)
            heap.heap_delete(element_in_heap)
            element_to_insert = new_score_node if new_score_node[1] < element_in_heap[1] else element_in_heap
            heap.heap_insert(element_to_insert)
        else:
            heap.heap_insert(new_score_node)

def visit_next_node(distances,graph,heap):
    if len(heap.heap) < 1:
        return None
    next_weight_node_visited = heap.heap_pop()
    distances[next_weight_node_visited[0]] = next_weight_node_visited[1]
    update_heap(graph, next_weight_node_visited[0], distances, heap)
    return next_weight_node_visited

if __name__ == "__main__":
    pass