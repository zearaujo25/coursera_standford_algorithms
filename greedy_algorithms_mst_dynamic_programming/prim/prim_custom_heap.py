from heap import Heap

def prim_custom_heap(graph,s):
    minimum_spanning_tree = {}
    minimum_spanning_tree[s] = set()
    heap = Heap(heap_type='min')
    update_heap(graph, s, minimum_spanning_tree, heap)
    while len(minimum_spanning_tree) != len(graph):
            edge_visited = visit_next_node(minimum_spanning_tree,graph,heap)
            if edge_visited is None:
                #no reachable node
                break
    return minimum_spanning_tree

def update_heap(graph, origin_node, minimum_spanning_tree, heap):
    for edge in graph[origin_node]:
        node = edge[0]
        if node in minimum_spanning_tree:
            continue
        else:
            print("Adding node: {}".format(node))
            heap.heap_insert(edge+(origin_node,))

def visit_next_node(minimun_spanning_tree,graph,heap): 
    if len(heap.heap) < 1:
        return None
    edge = heap.heap_pop()
    origin_node = edge[2]
    weight = edge[1]
    destination_node = edge[0]
    while destination_node in minimun_spanning_tree:
        edge = heap.heap_pop()
        if len(heap.heap) < 1:
            return None    
        origin_node = edge[2]
        weight = edge[1]
        destination_node = edge[0]
    minimun_spanning_tree[destination_node] = set()
    minimun_spanning_tree[destination_node].add((origin_node,weight))
    minimun_spanning_tree[origin_node].add(edge[:2])
    update_heap(graph, destination_node, minimun_spanning_tree, heap)
    return edge

if __name__ == "__main__":
    pass