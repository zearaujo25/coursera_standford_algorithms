from node import Node
from edge import Edge
class Graph:
    def __init__(self,graph_id = None):
        #dictionary containing the adjacent list
        self.adjacent_list = {}
        self.graph_id = graph_id
        
    def add_node(self,node):
        if node not in self.get_nodes():
            self.adjacent_list[node] = set()

    def remove_nodes(self,nodes):
        for node in nodes:
            del self.adjacent_list[node]

    def add_edge(self,edge):
        if edge not in self.get_edges():
            edge_nodes = list(edge.nodes)
            self.adjacent_list[edge_nodes[0]].add(edge)
            if not edge.is_self_edge():
                self.adjacent_list[edge_nodes[1]].add(edge)
    

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

    def read_graph_from_adjacent_list_file(self,graph_path):
        test_case = Graph()
        with open(graph_path) as f: 
            seen_nodes = {}
            for line in f: 
                
                line_nodes = line.split()
                node_id = int(line_nodes[0])
                print("Seen nodes: {}".format(seen_nodes))
                if node_id not in seen_nodes.keys():
                    print("adding new node: {}".format(node_id))
                    line_node = Node(node_id=node_id)
                    test_case.add_node(line_node)
                    seen_nodes[node_id] = line_node

                for edge_node_string in line_nodes[1:]:
                    edge_node_id = int(edge_node_string)
                    print("Seen nodes: {}".format(seen_nodes))
                    if edge_node_id not in seen_nodes.keys():
                        print("adding new end_node: {}".format(edge_node_id))
                        edge_node = Node(node_id=edge_node_id)
                        test_case.add_node(edge_node)
                        new_edge = Edge(edge_node,seen_nodes[node_id])
                        test_case.add_edge(new_edge)
                        seen_nodes[edge_node_id] = edge_node
        print("Seen nodes: {}".format(seen_nodes))
        return test_case
    def __str__(self):
        output = "-------------------\nGraphId: {}\n Graph:\n".format(self.graph_id)
        for node in self.adjacent_list.keys():
            edges = []
            for edge in self.adjacent_list[node]:
                edges.append(str(edge))
            output += "Node: {} | Edges: [{}]\n".format(str(node),str(edges))
        
        return output +  "-------------------\n"
