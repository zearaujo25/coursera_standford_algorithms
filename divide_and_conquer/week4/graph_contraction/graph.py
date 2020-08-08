class Graph:
    def __init__(self):
        #dictionary containing the adjacent list
        self.adjacent_list = {}
        
    def add_node(self,node):
        if node not in self.get_nodes():
            self.adjacent_list[node] = {}

    def add_edge(self,edge):
        if edge not in self.get_edges():
            edge_nodes = edge.nodes
            self.add_node(edge_nodes[0])
            self.add_node(edge_nodes[1])
            self.adjacent_list[edge_nodes[0]].add(edge)
            self.adjacent_list[edge_nodes[1]].add(edge)

    def get_nodes(self):
        return self.adjacent_list.keys()
        
    def get_edges(self):
        return set([edge for edge_List in self.adjacent_list.values() for edge in edge_List])
