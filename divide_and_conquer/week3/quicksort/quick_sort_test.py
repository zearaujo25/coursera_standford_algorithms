from quick_sort import quick_sort


import unittest

class QuickSortTest(unittest.TestCase):

    def totally_unordered_test(self):
        test_case = [9,8,7,6,5,4,3,2,1,0]
        ordered = [0,1,2,3,4,5,6,7,8,9]
        quick_sort(test_case)
        self.assertEqual(ordered,test_case,"Array not sorted: {}".format(test_case)) 

    def ordered_test(self):
        test_case = [0,1,2,3,4,5,6,7,8,9]
        ordered = [0,1,2,3,4,5,6,7,8,9]
        quick_sort(test_case)
        self.assertEqual(ordered,test_case,"Array not sorted: {}".format(test_case)) 

    def partially_ordered_test(self):
        test_case = [5,6,7,8,9,0,1,2,3,4]
        ordered = [0,1,2,3,4,5,6,7,8,9]
        quick_sort(test_case)
        self.assertEqual(ordered,test_case,"Array not sorted: {}".format(test_case)) 


if __name__ == '__main__':
    unittest.main()

