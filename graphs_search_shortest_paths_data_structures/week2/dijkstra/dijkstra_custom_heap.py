from heap import Heap
#this algorythm is O(m*n) because it needs to update all the references of the heap everytime there is a heapfy. to make a true mlogn, it is needed to ahve a custome heap that updates the reference at the same time heapfy goes
def dijkstra_custom_heap(graph,s):
    distances = {}
    distances[s] = 0
    heap = Heap(heap_type='min')
    heap_position = {}
    update_heap(graph, s, distances, heap_position, heap)
    while len(distances) != len(graph):
            node_weight_visited = visit_next_node(distances,graph,heap,heap_position)
            if node_weight_visited is None:
                #no reachable node
                break
    return distances

def update_heap(graph, next_node, distances, heap_position, heap):
    for edge in graph[next_node]:
        node = edge[0]
        weight = edge[1]
        node_score = distances[next_node] +weight
        new_score_node = (node_score,node)
        if node in distances:
            continue
        if node in heap.position_map:
            #update heap
            element_in_heap = heap.get_node_element[node]
            heap.heap_delete(element_in_heap)
            element_to_insert = new_score_node if new_score_node[1] < element_in_heap[1] else element_in_heap
            heap.heap_insert(element_to_insert)
        else:
            heap.heap_insert(new_score_node)

def visit_next_node(distances,graph,heap,heap_position):
    if len(heap) < 1:
        return None
    next_weight_node_visited = heap.heap_pop()
    distances[next_weight_node_visited[1]] = next_weight_node_visited[0]
    update_heap(graph, next_weight_node_visited[1], distances, heap_position, heap)
    return next_weight_node_visited

if __name__ == "__main__":
    pass