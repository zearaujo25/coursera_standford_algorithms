import unittest
import os
from cluster_nodes_only import ClusterNodesOnly


def read_cluster_graph(graph_path):
    cluster_graph = ClusterNodesOnly()
    with open(graph_path) as f: 
        for line in f: 
            node_bits = line.strip("\n").strip(" ")
            if len(node_bits) < 24:
                continue
            cluster_graph.add_node(node_bits)

    
    return cluster_graph

def get_assignment_answer(result_graph):

    return result_graph.get_maximum_spacing()

def get_test_inputs(path):
    inputs = []
    for file in os.listdir(path):
        if  "input" in file:
            inputs.append(os.path.join(path, file))
    inputs.sort()
    return inputs

def read_output(test_case_path):
    with open(test_case_path.replace("input","output")) as f: 
       for maximum_spacing in f: 
           return int(maximum_spacing)



class TestClusterGraph(unittest.TestCase):

    def test_coursera_question1(self):
        inputs = get_test_inputs("greedy_algorithms_mst_dynamic_programming/week2/clustering/test_cases/question2")
        for test_input in inputs:
            test_input = "greedy_algorithms_mst_dynamic_programming/week2/clustering/test_cases/question2/input_random_1_4_14.txt"
            print("Testing "+ test_input)
            test_case = read_cluster_graph(test_input)
            expected = read_output(test_input)
            final_answer = test_case.clusterfy()
            self.assertEqual(expected,final_answer)
            print("Test OK")
            break
    def test_assigment2(self):
        test_input = 'greedy_algorithms_mst_dynamic_programming/week2/clustering/assigment2.txt'
        print("Testing Assigment")
        test_case = read_cluster_graph(test_input)
        final_answer = test_case.clusterfy()
        print(final_answer)

if __name__ == "__main__":
    unittest.main()