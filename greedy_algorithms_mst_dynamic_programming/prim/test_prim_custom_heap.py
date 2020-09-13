import unittest
import os
from prim_custom_heap import prim_custom_heap

def read_graph(graph_path,sep=" "):
    graph = {}
    with open(graph_path) as f: 
        for line in f: 
            split_line = line.strip("\n").split(sep=sep)
            if len(split_line) < 3:
                continue
            node1 = int(split_line[0])
            node2 = int(split_line[1])
            weight = int(split_line[2])
            if node1 in graph:
                graph[node1].add((node2,weight))
            else:
                graph[node1] = set()
                graph[node1].add((node2,weight))

            if node2 in graph:
                graph[node2].add((node1,weight))
            else:
                graph[node2] = set()
                graph[node2].add((node1,weight))          
    
    return graph

def get_assignment_answer(result_mst):
    accumulated_weight = 0
    seen_edges = set()
    for node in result_mst:
        for edge in result_mst[node]:
            destination_node = edge[0]
            weight = edge[1]
            if (node,destination_node,weight) not in seen_edges and (destination_node,node,weight) not in seen_edges:
                seen_edges.add((node,destination_node,weight))
                seen_edges.add((destination_node,node,weight))
                accumulated_weight+=weight
    return accumulated_weight

def get_test_inputs(path):
    inputs = []
    for file in os.listdir(path):
        if  "input" in file:
            inputs.append(os.path.join(path, file))
    inputs.sort()
    return inputs

def read_output(test_case_path):
    with open(test_case_path.replace("input","output")) as f: 
       for cost in f: 
           return int(cost)



class TestPrim(unittest.TestCase):
    def test_prim_coursera_test_cases(self):
        inputs = get_test_inputs("greedy_algorithms_mst_dynamic_programming/prim/tests_cases")
        for test_input in inputs:
            test_input = 'greedy_algorithms_mst_dynamic_programming/prim/tests_cases/input_random_10_40.txt'
            print("Testing "+ test_input)
            test_case = read_graph(test_input," ")
            print(test_case)
            expected = read_output(test_input)
            result_mst = prim_custom_heap(test_case,1)
            print(result_mst)
            final_answer = get_assignment_answer(result_mst)
            self.assertEqual(expected,final_answer)
            print("Test OK")
            break
            

    def test_assigment(self):
        print("Testing Assigment")
        test_case = read_graph("greedy_algorithms_mst_dynamic_programming/prim/assigment.txt"," ")
        result_distances = prim_custom_heap(test_case,1)
        print(get_assignment_answer(result_distances))
        print("Test OK")

if __name__ == "__main__":
    unittest.main()