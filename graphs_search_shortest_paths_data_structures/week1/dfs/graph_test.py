import unittest
from graph import Graph
from node import Node
from edge import Edge

class TestGraph(unittest.TestCase):
    
    def test_adding_node(self):
        test_case = Graph()
        n_nodes = 10
        for i in range(n_nodes):
            test_node = Node(node_id=i)
            test_case.add_node(test_node)
        nodes = test_case.get_nodes()
        self.assertEqual(n_nodes,len(nodes))
        seen_nodes = set()
        for node in nodes:
            seen_nodes.add(node.node_id)
        self.assertEqual(n_nodes,len(seen_nodes))

    def test_adding_nodes(self):
        test_case = Graph()
        n_nodes = 10
        nodes_to_add = [Node(node_id=i) for i in range(n_nodes) ] 

        test_case.add_nodes(nodes_to_add) 

        nodes = test_case.get_nodes()
        self.assertEqual(n_nodes,len(nodes))
        seen_nodes = set()
        for node in nodes:
            seen_nodes.add(node.node_id)
        self.assertEqual(n_nodes,len(seen_nodes))


    def test_removing_node(self):
        test_case = Graph()
        test_node = Node(node_id=1)

        test_case.add_node(test_node)
        test_case.remove_nodes([test_node])
        
        nodes = test_case.get_nodes()
        self.assertEqual(0,len(nodes))

    def test_add_undirected_edge(self):
        test_case = Graph()
        
        test_node1 = Node(node_id=1)
        test_node2 = Node(node_id=2)
        test_case.add_node(test_node1)
        test_case.add_node(test_node2)
        
        test_edge = Edge(node1=test_node1,node2=test_node2)
        test_case.add_undirected_edge(test_edge)

        edges = test_case.get_edges()
        self.assertEqual(1,len(edges))

    def test_remove_undirected_edge(self):
        test_case = Graph()
        
        test_node1 = Node(node_id=1)
        test_node2 = Node(node_id=2)
        test_case.add_node(test_node1)
        test_case.add_node(test_node2)
        
        test_edge = Edge(node1=test_node1,node2=test_node2)
        test_case.add_undirected_edge(test_edge)
        test_case.remove_edge(test_edge)
        
        edges = test_case.get_edges()
        self.assertEqual(0,len(edges))

    def test_remove_self_edge(self):
        test_case = Graph()
        
        test_node1 = Node(node_id=1)
        test_case.add_node(test_node1)
        
        test_edge = Edge(node1=test_node1,node2=test_node1)
        test_case.add_undirected_edge(test_edge)
        test_case.remove_edge(test_edge)
        
        edges = test_case.get_edges()
        self.assertEqual(0,len(edges))

    def test_reassign_edge(self):
        test_case = Graph()
        
        test_node1 = Node(node_id=1)
        test_node2 = Node(node_id=2)
        test_node3 = Node(node_id=3)
        test_edge_1_3 = Edge(test_node1,test_node3)
        test_edge_2_3 = Edge(test_node2,test_node3)

        test_case.add_node(test_node1)
        test_case.add_node(test_node2)
        test_case.add_node(test_node3)
        test_case.add_undirected_edge(test_edge_1_3)
        test_case.add_undirected_edge(test_edge_2_3)

        test_super_node = Node()
        test_case.add_node(test_super_node)
        
        test_case.reassign_edges([test_node1,test_node2],test_super_node)

        test_super_node_edges = test_case.get_node_edges(test_super_node)
        test_node1_edges = test_case.get_node_edges(test_node1)
        test_node2_edges = test_case.get_node_edges(test_node2)
        test_node3_edges = test_case.get_node_edges(test_node3)

        self.assertTrue(len(test_super_node_edges) == 2)
        self.assertTrue(len(test_node1_edges) == 0)
        self.assertTrue(len(test_node2_edges) == 0)
        self.assertTrue(len(test_node3_edges) == 2)

    def test_clean_self_edge(self):
        test_case = Graph()
        
        test_node1 = Node(node_id=1)
        test_node2 = Node(node_id=2)
        test_edge_1_1_1 = Edge(test_node1,test_node1)
        test_edge_1_1_2 = Edge(test_node1,test_node1)
        test_edge_1_2 = Edge(test_node1,test_node2)

        test_case.add_node(test_node1)
        test_case.add_node(test_node2)
        test_case.add_undirected_edges([test_edge_1_1_1,test_edge_1_1_2,test_edge_1_2])
        
        test_case.clean_self_edges(test_node1)

        test_node1_edges = test_case.get_node_edges(test_node1)
        test_node2_edges = test_case.get_node_edges(test_node2)

        self.assertTrue(len(test_node1_edges) == 1)
        self.assertTrue(len(test_node2_edges) == 1)

    def test_add_direct_edge(self):
        test_case = Graph()
        
        test_node1 = Node(node_id=1)
        test_node2 = Node(node_id=2)
        test_case.add_node(test_node1)
        test_case.add_node(test_node2)
        
        test_edge = Edge(node1=test_node1,node2=test_node2)
        test_case.add_direct_edge(test_node1,test_edge)

        edges = test_case.get_edges()
        self.assertEqual(1,len(edges))
        self.assertEqual(1,len(test_case.get_node_edges(test_node1)))
        self.assertEqual(0,len(test_case.get_node_edges(test_node2)))

    def test_reversed(self):
        test_case = Graph()
        
        test_node1 = Node(node_id=1)
        test_node2 = Node(node_id=2)
        test_case.add_node(test_node1)
        test_case.add_node(test_node2)
        
        test_edge = Edge(node1=test_node1,node2=test_node2)
        test_case.add_direct_edge(test_node1,test_edge)

        test_result = test_case.get_reversed()
        
        self.assertEqual(test_case.get_nodes(),test_result.get_nodes())
        self.assertEqual(test_case.get_edges(),test_result.get_edges())

        self.assertEqual(1,len(test_case.get_node_edges(test_node1)))
        self.assertEqual(0,len(test_case.get_node_edges(test_node2)))

        self.assertEqual(1,len(test_result.get_node_edges(test_node2)))
        self.assertEqual(0,len(test_result.get_node_edges(test_node1)))

    def test_contract(self):
        test_case = Graph()
        
        test_node1 = Node(node_id=1)
        test_node2 = Node(node_id=2)
        test_node3 = Node(node_id=3)
        test_edge_1_3 = Edge(test_node1,test_node3)
        test_edge_1_2 = Edge(test_node1,test_node2)
        test_edge_2_3 = Edge(test_node2,test_node3)

        test_case.add_node(test_node1)
        test_case.add_node(test_node2)
        test_case.add_node(test_node3)
        test_case.add_undirected_edges([test_edge_1_3,test_edge_1_2,test_edge_2_3])



        result_node = test_case.contract(test_edge_1_2)

        test_result_node_edges = test_case.get_node_edges(result_node)
        test_node3_edges = test_case.get_node_edges(test_node3)

        self.assertTrue(len(test_result_node_edges) == 2)
        self.assertTrue(len(test_node3_edges) == 2)
        self.assertTrue(len(result_node.nodes_contracted) ==2)

    def test_read_graph_from_file(self):
        test_graph_path = 'divide_and_conquer/week4/graph_contraction/test_cases/input_random_1_6.txt'
        test_case = Graph(test_graph_path)
        self.assertEqual(6,len(test_case.get_nodes()))
        self.assertEqual(9,len(test_case.get_edges()))

        for node in test_case.get_nodes():

            node_edges = test_case.get_node_edges(node)
            if node.node_id == 1 :
                self.assertEqual(3,len(node_edges),"node failed: {}, Edges: {} ".format(node.node_id,[str(edge) for edge in node_edges]))
            elif node.node_id == 2: 
                self.assertEqual(4,len(node_edges),"node failed: {}, Edges: {} ".format(node.node_id,[str(edge) for edge in node_edges]))
            elif node.node_id == 3: 
                self.assertEqual(2,len(node_edges),"node failed: {}, Edges: {} ".format(node.node_id,[str(edge) for edge in node_edges]))
            elif node.node_id == 4: 
                self.assertEqual(3,len(node_edges),"node failed: {}, Edges: {} ".format(node.node_id,[str(edge) for edge in node_edges]))
            elif node.node_id == 5:                
                self.assertEqual(4,len(node_edges),"node failed: {}, Edges: {} ".format(node.node_id,[str(edge) for edge in node_edges]))
            elif node.node_id == 6:
                self.assertEqual(2,len(node_edges),"node failed: {}, Edges: {} ".format(node.node_id,[str(edge) for edge in node_edges]))
            else:
                raise Exception("Wrong Id")

if __name__ == "__main__":
    unittest.main()