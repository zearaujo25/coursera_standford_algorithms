from node import Node
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
            self.add_node(edge_nodes[0])
            self.add_node(edge_nodes[1])
            self.adjacent_list[edge_nodes[0]].add(edge)
            self.adjacent_list[edge_nodes[1]].add(edge)

    def get_nodes(self):
        return self.adjacent_list.keys()

    def get_edges(self):
        return set([edge for edge_List in self.adjacent_list.values() for edge in edge_List])
    
    def remove_edge(self,edge):
        nodes = edge.nodes
        self.adjacent_list[nodes[0]].remove(edge)
        if nodes[0] != nodes[1]:
            self.adjacent_list[nodes[1]].remove(edge)

    def reassing_edges(self,nodes,super_node):
        for node in nodes:
            for edge in self.adjacent_list[node]:
                edge.change_node(node,super_node)
                self.adjacent_list[super_node].add(edge)

    def clean_self_edges(self,node):
        for edge in self.adjacent_list[node]:
            edge_nodes = edge.nodes
            if edge_nodes[0] == edge_nodes[1]:
                self.remove_edge(edge)


    def contract(self,edge):
        self.remove_edge(edge)
        nodes = edge.get_nodes()
        super_node = Node(nodes_contracted=nodes)
        self.add_node(super_node)
        self.reassing_edges(nodes,super_node)
        self.clean_self_edges(super_node)
        self.remove_nodes(nodes)
    
    def __str__(self):
        output = "-------------------\nGraphId: {}\n Graph:\n".format(self.graph_id)
        for node in self.adjacent_list.keys():
            edges = []
            for edge in self.adjacent_list[node]:
                edges.append(str(edge))
            output += "Node: {} | Edges: [{}]\n".format(str(node),str(edges))
        
        return output +  "-------------------\n"
