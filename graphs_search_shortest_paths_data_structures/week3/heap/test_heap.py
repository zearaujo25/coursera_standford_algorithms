import unittest
from heap import heap_insert,heap_extract_min


class TestHeap(unittest.TestCase):
    def test_heap_insert(self):
        test_case = [i for i in range(10,0,-1)]
        test_heap = []
        test_position_map = {}

        for test_element in test_case:
            heap_insert(test_heap,test_position_map,test_element)
            self.assertEqual(test_element,test_heap[0])
        self.assertEqual(len(test_case),len(test_heap))

    def test_heap_extract_min(self):
        test_case = [i for i in range(10,0,-1)]
        test_heap = []
        test_position_map = {}
        correct_order = [i for i in range(1,11)]
        test_answer = []
        for test_element in test_case:
            heap_insert(test_heap,test_position_map,test_element)
        
        while len(test_heap) > 0:
            test_answer.append(heap_extract_min(test_heap,test_position_map))
        self.assertEqual(correct_order,test_answer)
        
if __name__ == "__main__":
    unittest.main()