from union_find import UnionFind

class ClusterGraph():
    def __init__(self):
        self.edges = []
        self.union_find = UnionFind()

    def add_edge(self,edge):
        self.edges.append(edge)
        self.union_find.add_element(edge[0])
        self.union_find.add_element(edge[1])

    def sort_edges(self):
        self.edges.sort(key= lambda edge: edge[2])


    def clusterfy(self,edges,num_clusters=4):
        self.sort_edges()
        while len(self.union_find.clusters) > num_clusters:
            edge = self.edges.pop()
            leader1 = self.union_find.find(edge[0])
            leader2 = self.union_find.find(edge[1])
            if leader1 != leader2:
                self.union_find.union(leader1,leader2)
    def get_maximum_spacing(self):
        return max(self.edges,key= lambda edge: edge[2])
    
