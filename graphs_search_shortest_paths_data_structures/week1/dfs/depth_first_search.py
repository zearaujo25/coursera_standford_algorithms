from queue import LifoQueue,Queue
from collections import deque
import sys 
from time import sleep
sys.setrecursionlimit(0x100000)


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
        self.global_time = 0
        for label,node in enumerate(graph.get_nodes()):
            self.f[label+1] = node

    def find_strongly_connected_components(self):
        reversed_graph = self.graph.get_reversed()
        self.dfs_loop(reversed_graph)
        self.dfs_loop(self.graph)

    def dfs(self,graph,start_node):
        self.explored.add(start_node)
        self.leaders[self.curren_leader_node].add(start_node)
        search_stack = deque()
        search_stack.append(start_node)
        while len(search_stack)>0:
            next_node = search_stack.pop()
            #A node only will be done if all its adjacents are explored
            is_done = True
            
            for edge in graph.get_node_edges(next_node):
                destination = edge.get_destination(next_node)
                if destination not in self.explored:
                    search_stack.append(next_node)
                    search_stack.append(destination)
                    
                    self.explored.add(destination)
                    self.leaders[self.curren_leader_node].add(destination)
                    is_done = False
                    #you cant explore other nodes withou finishin the new one, so we exit the loop
                    break

            if is_done:
                self.global_time +=1  
                self.new_f[self.global_time ] = next_node

    def dfs_loop(self,graph):
        self.global_time = 0
        self.curren_leader_node = None
        self.leaders.clear()
        self.explored.clear()
        for label in range(len(self.f), 0, -1):
            current_node = self.f[label]
            if current_node not in self.explored:
                self.curren_leader_node = current_node
                self.leaders[self.curren_leader_node] = set()
                self.dfs(graph,current_node)
        for label in self.new_f:
            self.f[label] = self.new_f[label]
        
        self.new_f.clear()
                
    def get_leaders(self):
        return self.leaders.keys()
    
    def get_top_ordered_scc(self,top_n=5):

        ordered_leaders = {leader:len(nodes) for leader,nodes in self.leaders.items()}
        top_values = [ v for k, v in sorted(ordered_leaders.items(), key=lambda item: item[1],reverse=True)]

        while len(top_values)< top_n:
            top_values.append(0) 
        
        return top_values[:top_n]