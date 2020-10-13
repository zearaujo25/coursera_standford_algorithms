import unittest
import os
from johnson import johnson_shortest_path

def read_graph(graph_path,sep=" "):
    graph = {}
    line_number = 0
    with open(graph_path) as f: 
        for line in f: 
            split_line = line.strip("\n").split(sep=sep)
            if line_number == 0:
                for node in range(1,int(split_line[0])+1):
                    graph[node] = {'incoming_edges':set(),'leaving_edges':set()}
                line_number+=1
                continue
            node_out = int(split_line[0])
            node_in = int(split_line[1])
            edge_weight = int(split_line[2])
            graph[node_out]['leaving_edges'].add((node_out,node_in,edge_weight))
            graph[node_in]['incoming_edges'].add((node_out,node_in,edge_weight))
            line_number+=1
    return graph

def get_assignment_answer(test_result):
    if test_result is None:
        return None
    else:
        nodes_shortest_path = map(get_shortest_for_node,test_result.values())
        final_answer = min(nodes_shortest_path)
        return final_answer

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

class TestJohnson(unittest.TestCase):
    def test_coursera_cases(self):
        test_cases_path = 'shortest_path_revisited_np_problems/week1/test_cases'
        test__files = get_test_inputs(test_cases_path)
        for test_input in test__files:
            print("Testing "+ test_input)
            test_case = read_graph(test_input,sep=" ")
            expected = read_output(test_input)
            test_result = johnson_shortest_path(test_case)
            final_answer = get_assignment_answer(test_result)
            self.assertEqual(expected,final_answer)
            print("Test OK")

    # def test_assigment(self):
    #     test_cases_path = 'shortest_path_revisited_np_problems/week1/assigment'
    #     test__files = get_test_inputs(test_cases_path)
    #     for test_input in test__files:
    #         print("Testing Assigment: "+ test_input)
    #         test_case = read_graph(test_input,sep=" ")
    #         test_result = johnson_shortest_path(test_case)
    #         final_answer = get_assignment_answer(test_result)
    #         print("Assigment {} Answer: {}".format(test_input,final_answer))
    #         print("Test OK")
            
if __name__ == "__main__":
    unittest.main()