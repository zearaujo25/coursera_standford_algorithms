import unittest
from graph import Graph
from node import Node
from edge import Edge
from breadth_first_search import breadth_first_search,find_connected_components

class TestBFS(unittest.TestCase):
    def test_breadth_first_search_undirected_connected_graph(self):
        graph = Graph()
        test_nodes = [Node(node_id=0),Node(node_id=1),Node(node_id=2),Node(node_id=3)]
        test_edges = [Edge(test_nodes[0],test_nodes[1]),
                      Edge(test_nodes[0],test_nodes[2]),
                      Edge(test_nodes[1],test_nodes[2]),
                      Edge(test_nodes[2],test_nodes[3]),
                      Edge(test_nodes[3],test_nodes[3])]

        graph.add_nodes(test_nodes)
        graph.add_edges(test_edges)
        origin_node = test_nodes[0]
        breadth_first_search(graph,origin_node)

        self.assertTrue(origin_node.is_explored())
        self.assertEqual(0,origin_node.get_distance())

        self.assertTrue(test_nodes[3].is_explored())
        self.assertEqual(2,test_nodes[3].get_distance(),msg="Wrong distance for node: " +str(test_nodes[3]))
    
        self.assertTrue(test_nodes[1].is_explored())
        self.assertEqual(1,test_nodes[1].get_distance(),msg="Wrong distance for node: " +str(test_nodes[1]))

        self.assertTrue(test_nodes[2].is_explored())
        self.assertEqual(1,test_nodes[2].get_distance(),msg="Wrong distance for node: " +str(test_nodes[2]))
        


    def test_breadth_first_search_undirected_disconnected_graph(self):
        graph = Graph()
        test_nodes = [Node(node_id=0),Node(node_id=1),Node(node_id=2),Node(node_id=3)]
        test_edges = [Edge(test_nodes[0],test_nodes[1]),
                      Edge(test_nodes[0],test_nodes[2]),
                      Edge(test_nodes[1],test_nodes[2]),
                      Edge(test_nodes[3],test_nodes[3])]

        graph.add_nodes(test_nodes)
        graph.add_edges(test_edges)
        origin_node = test_nodes[0]
        breadth_first_search(graph,origin_node)

        self.assertTrue(origin_node.is_explored())
        self.assertEqual(0,origin_node.get_distance())

        self.assertFalse(test_nodes[3].is_explored())
        self.assertEqual(float("inf"),test_nodes[3].get_distance(),msg="Wrong distance for node: " +str(test_nodes[3]))
    
        self.assertTrue(test_nodes[1].is_explored())
        self.assertEqual(1,test_nodes[1].get_distance(),msg="Wrong distance for node: " +str(test_nodes[1]))

        self.assertTrue(test_nodes[2].is_explored())
        self.assertEqual(1,test_nodes[2].get_distance(),msg="Wrong distance for node: " +str(test_nodes[2]))
        



    def test_find_connected_components(self):
        graph = Graph()
        #Graph from https://d3c33hcgiwev3.cloudfront.net/_bc5d400c4401bb47019da53961937cea_slides_algo-graphs-bfs_typed.pdf?Expires=1597622400&Signature=SsHqQKe-GdB6sewmyOL9GC2KrOKfPF3qAzMW8TBOGboyWV9WgRWgnBEaYO5dYcTxMUmNf2bTL2cTuivPXePAZ0KwAyUGTHxy2SFCwt1pdz8MQ5GuMnu0opPpVxEdvsnrYdDVgjd3zsJGJY7Q0tymCr7TmPebMbhwv9dpR6jAELY_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A
        test_nodes =[Node(node_id=i) for i in range(10) ] 
        
        connection1 = [Edge(test_nodes[0],test_nodes[2]),
                      Edge(test_nodes[0],test_nodes[4]),
                      Edge(test_nodes[2],test_nodes[4]),
                      Edge(test_nodes[4],test_nodes[8]),
                      Edge(test_nodes[4],test_nodes[6])]

        connection2 = [Edge(test_nodes[1],test_nodes[3])]

        connection3 = [Edge(test_nodes[5],test_nodes[7]),
                      Edge(test_nodes[5],test_nodes[9]),
                      Edge(test_nodes[7],test_nodes[9])]

        graph.add_nodes(test_nodes)
        graph.add_edges(connection1)
        graph.add_edges(connection2)
        graph.add_edges(connection3)

        test_case = find_connected_components(graph)
        
        self.assertEqual(3,test_case)

if __name__ == "__main__":
    unittest.main()
