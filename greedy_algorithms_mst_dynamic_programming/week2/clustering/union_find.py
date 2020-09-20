class UnionFind():

    def __init__(self):
        self.node_leaders = {}
        self.clusters = {}
    
    def add_element(self,element):
        self.node_leaders[element] = element
        self.clusters[element] = set()
        self.clusters[element].add(element)

    def find(self,element):
        return self.node_leaders[element]

    def union(self,leader1,leader2):
        looser = leader1 if len(self.clusters[leader1]) <= len(self.clusters[leader2]) else leader2
        winner = leader1 if looser == leader2 else leader2
        for element in self.clusters[looser]:
            self.node_leaders[element] = winner
            self.clusters[winner].add(element)
        del self.clusters[looser]


