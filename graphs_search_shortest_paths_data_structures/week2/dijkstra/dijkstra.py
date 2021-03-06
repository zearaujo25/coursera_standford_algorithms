def dijkstra(graph,s):
    visited_nodes = set()
    distances = {}
    paths = {}

    distances[s] = 0
    paths[s] = []
    visited_nodes.add(s)
    while len(visited_nodes) != len(graph.keys()):
            next_node, next_distance, next_path = get_next_visited(visited_nodes, distances,paths,graph)
            if next_node is None:
                break
            visited_nodes.add(next_node)
            distances[next_node] = next_distance
            paths[next_node] = next_path

    return distances,paths

def get_next_visited(visited_nodes, distances, paths,graph):
    source_node = None
    next_node = None
    next_distance = float("inf")
    next_path = None
    min_edge = None
    for node in visited_nodes:
        for edge in graph[node]:
            head_node = edge[0]
            if distances[node] + edge[1] < next_distance and head_node not in visited_nodes:
                next_node = head_node
                source_node = node
                next_distance = distances[node] + edge[1]
                min_edge = edge

    if next_node is not None:
        next_path = paths[source_node].copy()
        next_path.append(min_edge[0])

    return next_node, next_distance, next_path
                





if __name__ == "__main__":
    pass