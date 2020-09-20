import unittest
import os
from cluster_graph import ClusterGraph


def read_cluster_graph(graph_path,sep=" "):
    cluster_graph = ClusterGraph()
    with open(graph_path) as f: 
        for line in f: 
            split_line = line.strip("\n").split(sep=sep)
            if len(split_line) < 3:
                continue
            node1 = int(split_line[0])
            node2 = int(split_line[1])
            weight = int(split_line[2])
            cluster_graph.add_edge((node1,node2,weight))

    
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
        inputs = get_test_inputs("greedy_algorithms_mst_dynamic_programming/week2/clustering/test_cases/question1")
        for test_input in inputs:
            print("Testing "+ test_input)
            test_case = read_cluster_graph(test_input," ")
            expected = read_output(test_input)
            test_case.clusterfy(num_clusters=4)
            final_answer = get_assignment_answer(test_case)
            self.assertEqual(expected,final_answer)
            print("Test OK")

    def test_assigment1(self):
        test_input = 'greedy_algorithms_mst_dynamic_programming/week2/clustering/assigment1.txt'
        print("Testing Assigment")
        test_case = read_cluster_graph(test_input," ")
        test_case.clusterfy(num_clusters=4)
        final_answer = get_assignment_answer(test_case)
        print(final_answer)

if __name__ == "__main__":
    unittest.main()