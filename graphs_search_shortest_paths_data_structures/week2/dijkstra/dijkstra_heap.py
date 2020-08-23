from heapq import heappush, heappop,heapify

def dijkstra_heap(graph,s):
    distances = {}
    distances[s] = 0
    heap = []
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
        if node in heap_position:
            #update heap
            min_score_node = heap[heap_position[node]] if heap[heap_position[node]][0] < new_score_node[0] else new_score_node
            heap[heap_position[node]] = min_score_node
            heapify(heap)
            update_position_dictionary(heap, heap_position) 
        else:
            heappush(heap,new_score_node)
            update_position_dictionary(heap, heap_position) 

def update_position_dictionary(heap, heap_position):
    heap_position.clear()
    for position,weigh_node in enumerate(heap):
        heap_position[weigh_node[1]] = position 

def visit_next_node(distances,graph,heap,heap_position):
    if len(heap) < 1:
        return None
    next_weight_node_visited = heappop(heap)
    update_position_dictionary(heap, heap_position)
    distances[next_weight_node_visited[1]] = next_weight_node_visited[0]
    update_heap(graph, next_weight_node_visited[1], distances, heap_position, heap)
    return next_weight_node_visited

if __name__ == "__main__":
    pass