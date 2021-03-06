from node import Node

class Edge:
    def __init__(self,node1,node2):
        self.nodes = {node1,node2}
        self.original_nodes = "Node1: {}, Node2: {}".format(node1.node_id,node2.node_id)
        
    def change_node(self,node_to_remove,node_to_add):
        self.nodes.remove(node_to_remove)
        self.nodes.add(node_to_add)

    def get_destination(self,node):
        if node not in self.nodes:
            raise Exception("Node not in edge")
        nodes = list(self.nodes)
        if len(nodes) > 1 :
            nodes.remove(node)
        
        return nodes[0]
    

    def is_self_edge(self):
        return len(self.nodes) == 1
    
    def __str__(self):
        return "Original nodes: {}".format(self.original_nodes)