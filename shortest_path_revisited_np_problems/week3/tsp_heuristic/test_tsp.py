import unittest
import os
from tsp import tsp
from math import floor

def read_graph(graph_path,sep=" "):
    graph = {}
    line_number = 0
    with open(graph_path) as f: 
        for line in f: 
            split_line = line.strip("\n").split(sep=sep)
            if line_number == 0:
                for node in range(1,int(split_line[0])+1):
                    graph[node] = None
                line_number+=1
                continue
            node_x = float(split_line[0])
            node_y = float(split_line[1])
            graph[line_number] = (node_x,node_y)
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

def get_assignment_answer(test_result):
    return floor(test_result)

class TestTSP(unittest.TestCase):
    def test_cousera_test_cases(self):
        test_cases_path = 'shortest_path_revisited_np_problems/week2/test_cases/'
        test__files = get_test_inputs(test_cases_path)
        for test_input in test__files:
            print("Testing "+ test_input)
            test_case = read_graph(test_input,sep=" ")
            expected = read_output(test_input)
            test_result = tsp(test_case)
            final_answer = get_assignment_answer(test_result)
            self.assertEqual(expected,final_answer)
            print("Test OK")
            
    def test_assigment(self):
        test_cases_path = 'shortest_path_revisited_np_problems/week2/assigment/'
        test__files = get_test_inputs(test_cases_path)
        for test_input in test__files:
            print("Testing Assigment: "+ test_input)
            test_case = read_graph(test_input,sep=" ")
            test_result = tsp(test_case)
            final_answer = get_assignment_answer(test_result)
            print("Assigment {} Answer: {}".format(test_input,final_answer))
            print("Test OK")

if __name__ == "__main__":
    unittest.main()