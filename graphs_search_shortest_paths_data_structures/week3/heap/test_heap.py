import unittest
from random import shuffle,seed
from heap import Heap
seed(42)

class TestHeap(unittest.TestCase):
    def test_min_heap_insert(self):
        test_case = [i for i in range(10,0,-1)]
        heap_type = 'min'
        test_heap = Heap(heap_type)
        
        for test_element in test_case:
            test_heap.heap_insert(test_element)
            self.assertEqual(test_element,test_heap.heap[0])
        self.assertEqual(len(test_case),len(test_heap.heap))

    def test_heap_extract_min(self):
        test_case = [i for i in range(10,0,-1)]
        heap_type = 'min'
        test_heap = Heap(heap_type)
        correct_order = [i for i in range(1,11)]
        test_answer = []
        
        for test_element in test_case:
            test_heap.heap_insert(test_element)
        
        while len(test_heap.heap) > 0:
            test_answer.append(test_heap.heap_pop())
        self.assertEqual(correct_order,test_answer)

    def test_heap_extract_min_big_random_array(self):
        array_size = 100000
        test_case = [i for i in range(array_size,0,-1)]
        shuffle(test_case)
        heap_type = 'min'
        test_heap = Heap(heap_type)
        correct_order = [i for i in range(1,array_size+1)]
        test_answer = []
        
        for test_element in test_case:
            test_heap.heap_insert(test_element)
        
        while len(test_heap.heap) > 0:
            test_answer.append(test_heap.heap_pop())
        self.assertEqual(correct_order,test_answer) 

    def test_max_heap_insert(self):
        test_case = [i for i in range(1,11)]
        heap_type = 'max'
        test_heap = Heap(heap_type)
        for test_element in test_case:
            test_heap.heap_insert(test_element)
            self.assertEqual(test_element,test_heap.heap[0])
        self.assertEqual(len(test_case),len(test_heap.heap))

    def test_heap_extract_max(self):
        test_case = [i for i in range(1,11)]
        heap_type = 'max'
        test_heap = Heap(heap_type)
        correct_order = [i for i in range(10,0,-1)]
        test_answer = []
        for test_element in test_case:
            test_heap.heap_insert(test_element)
        
        while len(test_heap.heap) > 0:
            test_answer.append(test_heap.heap_pop())
        self.assertEqual(correct_order,test_answer)

    def test_heap_extract_max_big_random_array(self):
        array_size = 100000
        test_case = [i for i in range(1,array_size+1)]
        shuffle(test_case)
        heap_type = 'max'
        test_heap = Heap(heap_type)
        correct_order = [i for i in range(array_size,0,-1) ]
        test_answer = []
        for test_element in test_case:
            test_heap.heap_insert(test_element)
        
        while len(test_heap.heap) > 0:
            test_answer.append(test_heap.heap_pop())
        self.assertEqual(correct_order,test_answer) 
    
    def test_assigment(self):
        heap_low = Heap(heap_type='max')
        heap_high = Heap(heap_type='min')
        medians = []
        counter = 0
        assigment_path = 'graphs_search_shortest_paths_data_structures/week3/heap/assignment/assignment.txt'
        with open(assigment_path) as f: 
            for line in f: 
                counter += 1 
                number = int(line)
                if len(heap_low.heap) == 0:
                    heap_low.heap_insert(number)
                elif number < heap_low.heap[0]:
                    heap_low.heap_insert(number)
                elif len(heap_high.heap) == 0:
                    heap_high.heap_insert(number)
                elif number > heap_high.heap[0]:
                    heap_high.heap_insert(number)
                else:
                    heap_low.heap_insert(number)
            
                while len(heap_low.heap) > len(heap_high.heap):
                    heap_high.heap_insert(heap_low.heap_pop())

                while len(heap_low.heap) < len(heap_high.heap):
                    heap_low.heap_insert(heap_high.heap_pop())
                
                medians.append(heap_low.heap[0])
        print(sum(medians)%10000)




if __name__ == "__main__":
    unittest.main()