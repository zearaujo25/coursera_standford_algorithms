class Node:
    def __init__(self,node_id=None,nodes_contracted = None):
        self.node_id = node_id
        nodes_to_add = {}
        if nodes_contracted is not None:
            for node in nodes_contracted:
                if len(node.nodes_contracted) > 0:
                    nodes_to_add.update(nodes_contracted)
                else:
                    nodes_to_add.update(node)
        self.nodes_contracted = nodes_to_add
    def __str__(self):
        nodes_contracted = []
        if self.nodes_contracted is not None:
            nodes_contracted = [node.id for node in self.nodes_contracted]
        return "NodeId: {}, Nodes_contracted:{}".format(self.node_id,nodes_contracted)     

        