from union_find import UnionFind

class ClusterNodesOnly():
    def __init__(self):
        self.nodes = set()
        self.main_union_find = UnionFind()
        self.one_distances = []
        self.two_distances = []

    def find_all_one_distances(self,node):
        possible_nodes = []
        for bit in range(0,len(node)):
            search_node = node
            bit_to_change = "0" if node[bit] == '1' else "1"
            search_node[bit] = bit_to_change
            if search_node in self.nodes:
                possible_nodes.append(search_node)

        return possible_nodes

    def find_all_two_distances(self,node):
        possible_nodes = []
        for first_bit in range(0,len(node)-1):
            for second_bit in range(1,len(node)):
                search_node = node
                first_bit_to_change = "0" if node[first_bit] == "1" else "1"
                second_bit_to_change = "0" if node[second_bit] == "1" else "1"
                search_node[first_bit] = first_bit_to_change
                search_node[second_bit] = second_bit_to_change
                if search_node in self.nodes:
                    possible_nodes.append(search_node)

        return possible_nodes

    def add_node(self,node):
        self.nodes.add(node)
        self.main_union_find.add_element(node)
        one_distances = self.find_all_one_distances(node)
        for close_node in one_distances:
            self.one_distances.append((node,close_node))
        two_distances = self.find_all_two_distances(node)
        for close_node in two_distances:
            self.two_distances.append((node,close_node))
    



    def clusterfy(self):
        while len(self.one_distances) > 0 and len(self.two_distances) > 0:
            nodes = self.get_next_pair_of_nodes()
            leader1 = self.main_union_find.find(nodes[0])
            leader2 = self.main_union_find.find(nodes[1])
            if leader1 != leader2:
                self.main_union_find.union(leader1,leader2)
            return len(self.main_union_find.clusters)


    def get_next_pair_of_nodes(self):
        if len(self.one_distances) > 0:
            return self.one_distances.pop()
        elif len(self.two_distances) > 0:
            return self.two_distances.pop()
        else:
            return None
