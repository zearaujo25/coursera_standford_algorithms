import unittest
from graph import Graph
from node import Node
from edge import Edge
from depth_first_search import depth_first_search,depth_first_search_recursive,topological_sort,SCCFinder

class TestDFS(unittest.TestCase):

    def test_depth_first_search_undirected_connected_graph(self):
        graph = Graph()
        test_nodes = [Node(node_id=0),Node(node_id=1),Node(node_id=2),Node(node_id=3)]
        test_edges = [Edge(test_nodes[0],test_nodes[1]),
                      Edge(test_nodes[0],test_nodes[2]),
                      Edge(test_nodes[1],test_nodes[2]),
                      Edge(test_nodes[2],test_nodes[3]),
                      Edge(test_nodes[3],test_nodes[3])]

        graph.add_nodes(test_nodes)
        graph.add_undirected_edges(test_edges)
        origin_node = test_nodes[1]
        depth_first_search(graph,origin_node)
        for node in test_nodes:
            self.assertTrue(node.is_explored())

    def test_depth_first_search_undirected_disconnected_graph(self):
        graph = Graph()
        test_nodes = [Node(node_id=0),Node(node_id=1),Node(node_id=2),Node(node_id=3)]
        test_edges = [Edge(test_nodes[0],test_nodes[1]),
                      Edge(test_nodes[0],test_nodes[2]),
                      Edge(test_nodes[1],test_nodes[2]),
                      Edge(test_nodes[3],test_nodes[3])]

        graph.add_nodes(test_nodes)
        graph.add_undirected_edges(test_edges)
        origin_node = test_nodes[1]
        depth_first_search(graph,origin_node)
        
        self.assertFalse(test_nodes[3].is_explored())
        self.assertEqual(float("inf"),test_nodes[3].get_distance())
        for node in test_nodes[:3]:
            self.assertTrue(node.is_explored())

    def test_depth_first_search_recursive_undirected_connected_graph(self):
        graph = Graph()
        test_nodes = [Node(node_id=0),Node(node_id=1),Node(node_id=2),Node(node_id=3)]
        test_edges = [Edge(test_nodes[0],test_nodes[1]),
                      Edge(test_nodes[0],test_nodes[2]),
                      Edge(test_nodes[1],test_nodes[2]),
                      Edge(test_nodes[2],test_nodes[3]),
                      Edge(test_nodes[3],test_nodes[3])]

        graph.add_nodes(test_nodes)
        graph.add_undirected_edges(test_edges)
        origin_node = test_nodes[1]
        depth_first_search_recursive(graph,origin_node)
        for node in test_nodes:
            self.assertTrue(node.is_explored())

    def test_depth_first_search_recursive_undirected_disconnected_graph(self):
        graph = Graph()
        test_nodes = [Node(node_id=0),Node(node_id=1),Node(node_id=2),Node(node_id=3)]
        test_edges = [Edge(test_nodes[0],test_nodes[1]),
                      Edge(test_nodes[0],test_nodes[2]),
                      Edge(test_nodes[1],test_nodes[2]),
                      Edge(test_nodes[3],test_nodes[3])]

        graph.add_nodes(test_nodes)
        graph.add_undirected_edges(test_edges)
        origin_node = test_nodes[1]
        depth_first_search_recursive(graph,origin_node)
        
        self.assertFalse(test_nodes[3].is_explored())
        for node in test_nodes[:3]:
            self.assertTrue(node.is_explored())

    def test_topological_sort(self):
        graph = Graph()
        test_nodes = [Node(node_id=0),Node(node_id=1),Node(node_id=2),Node(node_id=3)]

        graph.add_nodes(test_nodes)
        graph.add_direct_edge(test_nodes[0],Edge(test_nodes[0],test_nodes[1]))
        graph.add_direct_edge(test_nodes[0],Edge(test_nodes[0],test_nodes[2]))
        graph.add_direct_edge(test_nodes[1],Edge(test_nodes[1],test_nodes[3]))
        graph.add_direct_edge(test_nodes[2],Edge(test_nodes[2],test_nodes[3]))

        topological_sort(graph)

        self.assertEqual(1,test_nodes[0].get_distance())
        self.assertEqual(4,test_nodes[3].get_distance())
        self.assertTrue(test_nodes[2].get_distance() == 2 or test_nodes[2].get_distance() == 3)
        self.assertTrue(test_nodes[1].get_distance() == 2 or test_nodes[1].get_distance() == 3)

    def test_scc_finder(self):
        pass

if __name__ == "__main__":
    unittest.main()
