import unittest
import os
from knapsack import knapsack

def read_items(symbols_path,sep="\t"):
    items = []
    line_number = 0 
    sack_size = None
    with open(symbols_path) as f: 
        for line in f: 
            if line_number == 0:
                sack_size = int(line.split(sep=sep)[0])
                line_number+=1
                continue
            line_array = line.strip("\n").split(sep=sep)
            item_value = int(line_array[0])
            item_weight = int(line_array[1])
            items.append((item_value,item_weight))
            line_number+=1
    
    return sack_size,items

def get_assignment_answer(result_encoding):
    min_len = float("inf")
    max_len = float("-inf")
    for symbol in result_encoding:

        symbol_len = len(result_encoding[symbol])
        min_len = len(result_encoding[symbol]) if symbol_len < min_len else min_len 
        max_len = len(result_encoding[symbol]) if symbol_len > max_len else max_len 

    return [max_len,min_len]

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
            return int(answer) 


class TestKnapsack(unittest.TestCase):
    def test_coursera_cases(self):
        test_cases_path = 'greedy_algorithms_mst_dynamic_programming/week4/test_cases'
        test__files = get_test_inputs(test_cases_path)
        for test_input in test__files:
            print("Testing "+ test_input)
            test_case = read_items(test_input,sep=" ")
            expected = read_output(test_input)

            final_answer = knapsack(test_case[0],test_case[1])

            self.assertEqual(expected,final_answer)

            print("Test OK")
            
    def test_assigment1(self):
        print("Testing Assigment 1")
        test_input = 'greedy_algorithms_mst_dynamic_programming/week4/knapsack/assigment1.txt'
        test_case = read_items(test_input," ")
            
        final_answer = knapsack(test_case[0],test_case[1])

            

        print("Final Answer: {}".format(final_answer))

    def test_assigment2(self):
        print("Testing Assigment 2")
        test_input = 'greedy_algorithms_mst_dynamic_programming/week4/knapsack/assigment2.txt'
        test_case = read_items(test_input," ")
            
        final_answer = knapsack(test_case[0],test_case[1])

            

        print("Final Answer: {}".format(final_answer))



if __name__ == "__main__":
    unittest.main()