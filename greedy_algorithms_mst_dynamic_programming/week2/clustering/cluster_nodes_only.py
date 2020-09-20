from union_find import UnionFind

class ClusterNodesOnly():
    def __init__(self):
        self.union_find = UnionFind()
        self.one_distances = []
        self.two_distances = []

    def find_all_one_distances(self,node):
        possible_nodes = []
        for bit in range(0,len(node)):
            search_node = node.copy()
            bit_to_change = "0" if node[bit] == '1' else "1"
            search_node[bit] = bit_to_change
            if tuple(search_node) in self.union_find.node_leaders:
                possible_nodes.append(search_node)

        return possible_nodes

    def find_all_two_distances(self,node):
        possible_nodes = []
        for first_bit in range(0,len(node)-1):
            for second_bit in range(1,len(node)):
                search_node = node.copy()
                first_bit_to_change = "0" if node[first_bit] == "1" else "1"
                second_bit_to_change = "0" if node[second_bit] == "1" else "1"
                search_node[first_bit] = first_bit_to_change
                search_node[second_bit] = second_bit_to_change
                if tuple(search_node) in self.union_find.node_leaders:
                    possible_nodes.append(search_node)

        return possible_nodes

    def add_node(self,node):
        self.union_find.add_element(tuple(node))
        one_distances = self.find_all_one_distances(node)
        for close_node in one_distances:
            self.one_distances.append((node,close_node))
        two_distances = self.find_all_two_distances(node)
        for close_node in two_distances:
            self.two_distances.append((node,close_node))
    



    def clusterfy(self):
        while len(self.one_distances) > 0 or len(self.two_distances) > 0:
            nodes = self.get_next_pair_of_nodes()
            leader1 = self.union_find.find(tuple(nodes[0]))
            leader2 = self.union_find.find(tuple(nodes[1]))
            if leader1 != leader2:
                self.union_find.union(tuple(leader1),tuple(leader2))
        return len(self.union_find.clusters)


    def get_next_pair_of_nodes(self):
        if len(self.one_distances) > 0:
            return self.one_distances.pop()
        elif len(self.two_distances) > 0:
            return self.two_distances.pop()
        else:
            return None
