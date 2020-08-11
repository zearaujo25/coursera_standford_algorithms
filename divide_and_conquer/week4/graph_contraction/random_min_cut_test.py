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

def read_output(test_case_path):

    with open(test_case_path.replace("input","output")) as f: 
       for line in f: 
           return int(line)

def get_test_case(test_case_path):
    input_graph = Graph(test_case_path)
    min_cut_expected = read_output(test_case_path)
    return input_graph,min_cut_expected

class RandomMinCutTest(unittest.TestCase):
    
    # def test_coursera_test_cases(self):
    #     test_cases_dir = "divide_and_conquer/week4/graph_contraction/test_cases/"
    #     test_inputs = get_test_inputs(test_cases_dir)
    #     for test_input in test_inputs:
    #         print("Testing for "+test_input)
    #         input_graph,min_cut_expected = get_test_case(test_input)
    #         test_min_cut = random_contractions(input_graph)
    #         self.assertEqual(min_cut_expected,len(test_min_cut.get_edges()))
    #         print("Test OK")

    def test_assignment(self):

        print("Testing for assignment")
        test_input = "divide_and_conquer/week4/graph_contraction/assignment.txt"
        input_graph,min_cut_expected = Graph(test_input),17
        test_min_cut = random_contractions(input_graph)
        self.assertEqual(min_cut_expected,len(test_min_cut.get_edges()))
        print("Test OK")

if __name__ == "__main__":
    unittest.main()