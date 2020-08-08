from node import Node

class Edge:
    def __init__(self,node1,node2):
        self.nodes = {node1,node2}