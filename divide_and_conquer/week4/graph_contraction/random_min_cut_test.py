import unittest
from graph import Graph
from node import Node
from edge import Edge
from random_min_cut import random_contractions
import os

def get_test_inputs(path):
    inputs = []
    for file in os.listdir(path):
        if  "input" in file:
            inputs.append(os.path.join(path, file))
    return inputs

def read_test_graph(test_case_path):
    test_case = Graph()
    with open(test_case_path) as f: 
        seen_nodes = {}
        for line in f: 
            
            line_nodes = line.split()
            node_id = int(line_nodes[0])
            print("Seen nodes: {}".format(seen_nodes))
            if node_id not in seen_nodes.keys():
                print("adding new node: {}".format(node_id))
                line_node = Node(node_id=node_id)
                test_case.add_node(line_node)
                seen_nodes[node_id] = line_node

            for edge_node_string in line_nodes[1:]:
                edge_node_id = int(edge_node_string)
                print("Seen nodes: {}".format(seen_nodes))
                if edge_node_id not in seen_nodes.keys():
                    print("adding new end_node: {}".format(edge_node_id))
                    edge_node = Node(node_id=edge_node_id)
                    test_case.add_node(edge_node)
                    new_edge = Edge(edge_node,seen_nodes[node_id])
                    test_case.add_edge(new_edge)
                    seen_nodes[edge_node_id] = edge_node
    print("Seen nodes: {}".format(seen_nodes))
    return test_case
def read_output(test_case_path):

    with open(test_case_path.replace("input","output")) as f: 
       for line in f: 
           return int(line)

def get_test_case(test_case_path):
    input_graph = read_test_graph(test_case_path)
    min_cut_expected = read_output(test_case_path)
    return input_graph,min_cut_expected

class RandomMinCutTest(unittest.TestCase):
    
    def test_coursera_test_cases(self):
        test_cases_dir = "./test_cases"
        test_inputs = get_test_inputs(test_cases_dir)
        for test_input in test_inputs:
            # input_graph,min_cut_expected = get_test_case(test_input)
            input_graph,min_cut_expected = get_test_case("./test_cases/input_random_1_6.txt")
            print(input_graph,min_cut_expected)
            break
            #test_min_cut = random_contractions(input_graph)
            #self.assertEquals(min_cut_expected,len(test_min_cut.get_edges()))

if __name__ == "__main__":
    unittest.main()