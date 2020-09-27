from wis import wis
import unittest
import os

def read_input(input_path):
    input_nodes = []
    line_number = 0 
    with open(input_path) as f: 
        for line in f: 
            if line_number == 0:
                line_number+=1
                continue
            node_weight = int(line.strip("\n"))
            input_nodes.append(node_weight)
            line_number+=1

    return input_nodes

def get_assignment_answer(result_nodes):
    assigment_nodes = [1,2,3,4,17,117,517,997]
    return "".join(["1" if node-1 in result_nodes else "0" for node in assigment_nodes])

def get_test_inputs(path):
    inputs = []
    for file in os.listdir(path):
        if  "input" in file:
            inputs.append(os.path.join(path, file))
    inputs.sort()
    return inputs

def read_output(test_case_path):
    with open(test_case_path.replace("input","output")) as f: 
        for answer in f: 
            return answer

class TestWIS(unittest.TestCase):
    def test_coursera_cases(self):
        test_cases_path = 'greedy_algorithms_mst_dynamic_programming/week3/test_cases/huffman'
        test__files = get_test_inputs(test_cases_path)
        for test_input in test__files:

            print("Testing "+ test_input)
            test_case = read_input(test_input)
            expected = read_output(test_input)
            
            result  = wis(test_case)
            final_answer = get_assignment_answer(result)

            self.assertEqual(expected,final_answer)

            print("Test OK")

    # def test_assigment_1_2(self):
    #     print("Testing Assigment")
    #     test_input = 'greedy_algorithms_mst_dynamic_programming/week3/assigment1_2.txt'
    #     test_case = read_input(test_input)
            
    #     test_case.huffman_encode()
    #     encoding_map = test_case.create_encode_map_string()
    #     final_answer = get_assignment_answer(encoding_map)

            

    #     print("Final Answer: {}".format(final_answer))


if __name__ == "__main__":
    unittest.main()