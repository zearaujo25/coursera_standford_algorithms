from queue import LifoQueue
from copy import deepcopy
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
        if not destination.is_explored():
            current_label = depth_first_search_recursive(graph,destination,current_label)
    start_node.set_distance(current_label)
    return current_label-1 if current_label is not None else None
    
def topological_sort(graph):
    nodes = graph.get_nodes()
    current_label = len(nodes)
    for next_node in nodes:
        if not next_node.is_explored():
            depth_first_search_recursive(graph,next_node,current_label)







class SCCFinder():
    def __init__(self,graph):
        self.graph = graph
        self.explored = set()
        self.f = {}
        self.new_f = {}
        self.leaders = {}
        self.curren_leader_node = None
        self.time = 0
        for label,node in enumerate(graph.get_nodes()):
            self.f[label+1] = node

    def find_strongly_connected_components(self):
        reversed_graph = self.graph.get_reversed()
        self.dfs_loop(reversed_graph)
        self.dfs_loop(self.graph)

        
    def dfs(self,graph,current_node):
        
        self.explored.add(current_node)
        self.leaders[current_node] = self.curren_leader_node 
        
        for edge in graph.get_node_edges(current_node):
            destination_node = edge.get_destination(current_node)
            if not destination_node in self.explored:
                self.dfs(graph,destination_node)

        self.time +=1
        self.new_f[self.time] = current_node

    def dfs_loop(self,graph):
        self.time = 0
        self.curren_leader_node = None
        self.leaders.clear()
        self.explored.clear()
        for label in range(len(self.f), 0, -1):
            current_node = self.f[label]
            if current_node not in self.explored:
                self.curren_leader_node = current_node
                self.dfs(graph,current_node)
        self.f = deepcopy(self.new_f)
        self.new_f.clear()
                
