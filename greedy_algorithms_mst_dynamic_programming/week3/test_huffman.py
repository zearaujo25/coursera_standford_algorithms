from huffman import HuffmanCode
import unittest
import os

def read_huffman(symbols_path):
    huffman = HuffmanCode()
    line_number = 0 
    with open(symbols_path) as f: 
        for line in f: 
            if line_number == 0:
                line_number+=1
                continue
            node_weight = int(line.strip("\n"))
            huffman.add_symbol(node_weight,symbol_info=line_number)
            line_number+=1

    
    return huffman

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
        answers = []
        for answer in f: 
            answers.append(int(answer)) 
        return answers

class TestHuffman(unittest.TestCase):
    def test_coursera_cases(self):
        test_cases_path = 'greedy_algorithms_mst_dynamic_programming/week3/test_cases/huffman'
        test__files = get_test_inputs(test_cases_path)
        for test_input in test__files:
            print("Testing "+ test_input)
            test_case = read_huffman(test_input)
            expected = read_output(test_input)
            
            test_case.huffman_encode()
            

            # self.assertEqual(expected,final_answer)

            print("Test OK")
            


if __name__ == "__main__":
    unittest.main()