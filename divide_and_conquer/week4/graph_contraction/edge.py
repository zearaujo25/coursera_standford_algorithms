from node import Node

class Edge:
    def __init__(self,node1,node2):
        self.nodes = {node1,node2}
        self.original_nodes = "Node1: {}, Node2: {}".format(node1.node_id,node2.node_id)
        
    def change_node(self,node_to_remove,node_to_add):
        self.nodes.remove(node_to_remove)
        self.nodes.add(node_to_add)
    
    def __str__(self):
        return "Original nodes: {}".format(self.original_nodes)