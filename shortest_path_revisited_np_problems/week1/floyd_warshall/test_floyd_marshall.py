import unittest
import os
from floyd_marshall import floyd_marshall_all_shortest_paths

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

def get_assignment_answer(test_distance_result):
    nodes = [7,37,59,82,99,115,133,165,188,197]
    return [test_distance_result[node] for node in nodes]

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

def get_shortest_for_node(node_paths):
    paths = node_paths.values()
    return min(paths)

class TestFloydMarshall(unittest.TestCase):
    def test_coursera_cases(self):
        test_cases_path = 'shortest_path_revisited_np_problems/week1/test_cases'
        test__files = get_test_inputs(test_cases_path)
        for test_input in test__files:
            print("Testing "+ test_input)
            test_case = read_graph(test_input,sep=" ")
            expected = read_output(test_input)
            test_result = floyd_marshall_all_shortest_paths(test_case)
            if test_result is None:
                self.assertEqual(expected,test_result)
            else:
                nodes_shortest_path = map(get_shortest_for_node,test_result.values())
                final_answer = min(nodes_shortest_path)
                self.assertEqual(expected,final_answer)
            print("Test OK")
            
if __name__ == "__main__":
    unittest.main()