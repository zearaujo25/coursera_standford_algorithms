import unittest
import os
from bellman_ford import bellman_shortest_path

def read_graph(graph_path,sep=" "):
    graph = {}
    line_number = 0
    with open(graph_path) as f: 
        for line in f: 
            split_line = line.strip("\n").split(sep=sep)
            if line_number == 0:
                for node in range(1,int(split_line[0])+1):
                    graph[node] = {'incomming_edges':set(),'outgoing_edges':set()}
                line_number+=1
                continue
            node_out = int(split_line[0])
            node_in = int(split_line[1])
            edge_weight = int(split_line[2])
            graph[node_out]['outgoing_edges'].add((node_out,node_in,edge_weight))
            graph[node_in]['incomming_edges'].add((node_out,node_in,edge_weight))
            line_number+=1
    return graph

def get_test_inputs(path):
    inputs = []
    for file in os.listdir(path):
        if  "input" in file:
            inputs.append(os.path.join(path, file))
    return inputs

def read_output(test_case_path):
    with open(test_case_path.replace("input","output")) as f: 
       for line in f: 
           line = line.strip('\n')
           return int(line) if line != 'NULL' else None



class TestBellmanFord(unittest.TestCase):
    def test_negative_cicle(self):
        test_case = read_graph("shortest_path_revisited_np_problems/week1/test_cases/input_random_1_2.txt"," ")
        result_distances = bellman_shortest_path(test_case,1)
        self.assertEqual(None,result_distances)
    def test_small_case(self):
        test_case = read_graph("shortest_path_revisited_np_problems/week1/test_cases/input_random_2_2.txt"," ")
        result_distances = bellman_shortest_path(test_case,1)
        self.assertEqual(-66,min(result_distances.values()))

    def test_coursera_cases(self):
        test_cases_path = 'shortest_path_revisited_np_problems/week1/test_cases'
        test__files = get_test_inputs(test_cases_path)
        for test_input in test__files:
            print("Testing "+ test_input)
            test_case = read_graph(test_input,sep=" ")
            expected = read_output(test_input)
            min_array = []
            final_answer = None
            for node in test_case:
                node_result = bellman_shortest_path(test_case,node)
                if node_result is None:
                    break
                min_array.append(min(node_result.values()))
            
            final_answer = min(min_array) if len(min_array) > 0 else None
            self.assertEqual(expected,final_answer)

            print("Test OK")
            
if __name__ == "__main__":
    unittest.main()