import unittest
import os
from dijkstra import dijkstra

def read_graph(graph_path,sep=" "):
    graph = {}
    with open(graph_path) as f: 
        for line in f: 
            split_line = line.strip("\n").split(sep=sep)
            node = int(split_line[0])
            graph[node] = set()
            for edge in split_line[1:]:
                converted_edge = edge.split(",")
                if(len(converted_edge) > 1):
                    head_node = int(converted_edge[0])
                    weight = int(converted_edge[1])
                    graph[node].add((head_node,weight))
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
           return [int(leader) for leader in line.split(',')]



class TestDijkstra(unittest.TestCase):
    def test_dijkstra(self):
        test_case = read_graph("graphs_search_shortest_paths_data_structures/week2/dijkstra/test_cases/test_case_1.txt"," ")
        result_distances,result_paths = dijkstra(test_case,1)
        self.assertEqual(0,result_distances[1])
        self.assertEqual(1,result_distances[2])
        self.assertEqual(2,result_distances[3])
        self.assertEqual(3,result_distances[4])
        self.assertEqual(4,result_distances[5])
        self.assertEqual(4,result_distances[6])
        self.assertEqual(3,result_distances[7])
        self.assertEqual(2,result_distances[8])

        self.assertEqual([],result_paths[1])
        self.assertEqual([2],result_paths[2])
        self.assertEqual([2,3],result_paths[3])
        self.assertEqual([2,3,4],result_paths[4])
        self.assertEqual([2,3,4,5],result_paths[5])
        self.assertEqual([8,7,6],result_paths[6])
        self.assertEqual([8,7],result_paths[7])
        self.assertEqual([8],result_paths[8])    

    # def test_dijkstra_coursera_test_cases(self):
    #     inputs = get_test_inputs("graphs_search_shortest_paths_data_structures/week2/dijkstra/test_cases/coursera_tests")
    #     for test_input in inputs:
    #         print("Testing "+ test_input)
    #         test_case = read_graph(test_input,"\t")
    #         expected = read_output(test_input)
    #         result_distances = dijkstra(test_case,1)[0]
    #         final_answer = get_assignment_answer(result_distances)
    #         self.assertEqual(expected,final_answer)
    #         print("Test OK")

    def test_assigment(self):
        print("Testing Assigment")
        test_case = read_graph("graphs_search_shortest_paths_data_structures/week2/dijkstra/test_cases/assigment.txt","\t")
        result_distances = dijkstra(test_case,1)[0]
        print(get_assignment_answer(result_distances))
        print("Test OK")

if __name__ == "__main__":
    unittest.main()