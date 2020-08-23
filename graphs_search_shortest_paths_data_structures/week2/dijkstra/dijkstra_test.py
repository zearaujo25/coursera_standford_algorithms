import unittest
from dijkstra import dijkstra

def read_graph(graph_path):
    graph = {}
    with open(graph_path) as f: 
        for line in f: 
            split_line = line.split(sep=" ")
            node = int(split_line[0])
            graph[node] = set()
            for edge in split_line[1:]:
                converted_edge = edge.split(",")
                head_node = int(converted_edge[0])
                weight = int(converted_edge[1])
                graph[node].add((head_node,weight))
    return graph

class TestDijkstra(unittest.TestCase):
    def test_dijkstra(self):
        test_case = read_graph("graphs_search_shortest_paths_data_structures/week2/dijkstra/test_cases/test_case_1.txt")
        result_distances,result_paths = dijkstra(test_case,1)
        self.assertEqual(0,result_distances[1])
        self.assertEqual(1,result_distances[2])
        self.assertEqual(2,result_distances[3])
        self.assertEqual(3,result_distances[4])
        self.assertEqual(4,result_distances[5])
        self.assertEqual(4,result_distances[6])
        self.assertEqual(3,result_distances[7])
        self.assertEqual(2,result_distances[8])

        self.assertEqual([],result_paths[1])
        self.assertEqual([2],result_paths[2])
        self.assertEqual([2,3],result_paths[3])
        self.assertEqual([2,3,4],result_paths[4])
        self.assertEqual([2,3,4,5],result_paths[5])
        self.assertEqual([8,7,6],result_paths[6])
        self.assertEqual([8,7],result_paths[7])
        self.assertEqual([8],result_paths[8])    



if __name__ == "__main__":
    unittest.main()