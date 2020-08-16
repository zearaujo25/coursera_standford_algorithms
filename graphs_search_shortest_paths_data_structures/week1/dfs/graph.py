from node import Node
from edge import Edge
class Graph:
    def __init__(self,graph_path = None):
        #dictionary containing the adjacent list
        self.adjacent_list = {}
        self.graph_id = graph_path
        if graph_path is not None:
            self.read_graph_from_adjacent_list_file(graph_path)
    def add_node(self,node):
        if node not in self.get_nodes():
            self.adjacent_list[node] = set()
    
    def add_nodes(self,nodes):
        for node in nodes:
            self.add_node(node)

    def remove_nodes(self,nodes):
        for node in nodes:
            del self.adjacent_list[node]
    
    def add_direct_edge(self,node,edge):
        self.adjacent_list[node].add(edge)

    def add_undirected_edge(self,edge):
        if edge not in self.get_edges():
            edge_nodes = list(edge.nodes)
            self.adjacent_list[edge_nodes[0]].add(edge)
            if not edge.is_self_edge():
                self.adjacent_list[edge_nodes[1]].add(edge)
    
    def add_undirected_edges(self,edges):
        for edge in edges:
            self.add_undirected_edge(edge)

    def get_nodes(self):
        return self.adjacent_list.keys()

    def get_edges(self):
        return set([edge for edge_List in self.adjacent_list.values() for edge in edge_List])
    
    def get_node_edges(self,node):
        return self.adjacent_list[node]
    
    def remove_edge(self,edge):
        nodes = list(edge.nodes)
        self.adjacent_list[nodes[0]].remove(edge)
        if not edge.is_self_edge():
            self.adjacent_list[nodes[1]].remove(edge)

    def reassign_edges(self,nodes,super_node):
        for node in nodes:
            for edge in self.adjacent_list[node].copy():
                edge.change_node(node,super_node)
                self.adjacent_list[super_node].add(edge)
                self.adjacent_list[node].remove(edge)

    def clean_self_edges(self,node):
        for edge in self.adjacent_list[node].copy():
            if edge.is_self_edge():
                self.remove_edge(edge)

    def contract(self,edge):
        self.remove_edge(edge)
        nodes = edge.nodes
        super_node = Node(nodes_contracted=nodes)
        self.add_node(super_node)
        self.reassign_edges(nodes,super_node)
        self.clean_self_edges(super_node)
        self.remove_nodes(nodes)
        return super_node

    def get_reversed(self):
        reversed_graph = Graph()
        for node in self.adjacent_list:
            reversed_graph.add_node(node)
            for edge in self.get_node_edges(node):
                detination_node = edge.get_destination(node)
                reversed_graph.add_node(detination_node)
                reversed_graph.add_direct_edge(detination_node,edge)
        return reversed_graph

    def read_graph_from_adjacent_list_file(self,graph_path):
        with open(graph_path) as f: 
            seen_nodes = {}
            seen_edges = {}
            for line in f: 
                line_nodes = line.split()
                node_id = int(line_nodes[0])
                if node_id not in seen_nodes.keys():
                    line_node = Node(node_id=node_id)
                    self.add_node(line_node)
                    seen_nodes[node_id] = line_node
                    seen_edges[node_id] = []

                for edge_node_string in line_nodes[1:]:
                    edge_node_id = int(edge_node_string)
                    if edge_node_id not in seen_nodes.keys():
                        edge_node = Node(node_id=edge_node_id)
                        self.add_node(edge_node)
                        seen_edges[edge_node_id] = []
                        seen_nodes[edge_node_id] = edge_node

                    if edge_node_id not in seen_edges[node_id]:
                        new_edge = Edge(seen_nodes[edge_node_id],seen_nodes[node_id])
                        self.add_undirected_edge(new_edge)
                        seen_edges[node_id].append(edge_node_id)
                        seen_edges[edge_node_id].append(node_id)

    def __str__(self):
        output = "-------------------\nGraphId: {}\n Graph:\n".format(self.graph_id)
        for node in self.adjacent_list.keys():
            edges = []
            for edge in self.adjacent_list[node]:
                edges.append(str(edge))
            output += "Node: {} | Edges: [{}]\n".format(str(node),str(edges))
        
        return output +  "-------------------\n"
