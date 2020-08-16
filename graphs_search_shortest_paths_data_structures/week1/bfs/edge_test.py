import unittest
from graph import Graph
from node import Node
from edge import Edge

class TestEdge(unittest.TestCase):
    def test_get_destination_success(self):
        from_node = Node()
        to_node = Node()
        test_case = Edge(from_node,to_node)
        test_result = test_case.get_destination(from_node)
        self.assertEqual(to_node,test_result,"Wrong destination")
    
    def test_get_destination_self_success(self):
        from_node = Node()
        to_node = from_node
        test_case = Edge(from_node,to_node)
        test_result = test_case.get_destination(from_node)
        self.assertEqual(to_node,test_result,"Wrong destination")

    def test_get_destination_fail(self):
        from_node = Node()
        to_node = Node()
        wrong_node = Node()
        test_case = Edge(from_node,to_node)
        self.assertRaises(Exception,test_case.get_destination,wrong_node)


if __name__ == "__main__":
    unittest.main()