from quick_sort import quick_sort
from quick_sort import choose_pivot_median,get_number_of_comparisons


import unittest

class QuickSortTest(unittest.TestCase):

    def totally_unordered_test(self):
        test_case = [9,8,7,6,5,4,3,2,1,0]
        ordered = [0,1,2,3,4,5,6,7,8,9]
        quick_sort(test_case)
        self.assertEqual(ordered,test_case,"Array not sorted") 

    def ordered_test(self):
        test_case = [0,1,2,3,4,5,6,7,8,9]
        ordered = [0,1,2,3,4,5,6,7,8,9]
        quick_sort(test_case)
        self.assertEqual(ordered,test_case,"Array not sorted") 

    def partially_ordered_test(self):
        test_case = [5,6,7,8,9,0,1,2,3,4]
        ordered = [0,1,2,3,4,5,6,7,8,9]
        quick_sort(test_case)
        self.assertEqual(ordered,test_case,"Array not sorted") 

    def test_order_median_method(self):
        test_case = [2, 20, 1, 15, 3, 11, 13, 6, 16, 10, 19, 5, 4, 9, 8, 14, 18, 17, 7, 12] 

        ordered = [2, 20, 1, 15, 3, 11, 13, 6, 16, 10, 19, 5, 4, 9, 8, 14, 18, 17, 7, 12]
        ordered.sort()
        true_count_number = 55
        test_count_number = quick_sort(test_case,pivot_method="median")

        self.assertEqual(ordered,test_case,"Array not sorted") 
        self.assertEqual(true_count_number,test_count_number,"Wrong number of counts: {}".format(test_count_number)) 

    def test_median_pivot_method(self):
       
        test_single_median_pivot(self,[2, 20, 1, 15, 3, 11, 13, 6, 16, 10, 19, 5, 4, 9, 8, 14, 18, 17, 7, 12],10 ) 
        test_single_median_pivot(self,[7, 1, 3, 6, 2, 5, 4, 9, 8] ,7 ) 
        test_single_median_pivot(self,[4, 1, 3, 6, 2, 5] ,4 ) 
        test_single_median_pivot(self,[2, 1, 3], 2) 
        test_single_median_pivot(self,[6, 5] , 6) 
    
    def test_get_number_of_comparisons(self):
        pass

def test_single_median_pivot(test,test_case,correct_median):

    median_index = choose_pivot_median(test_case,0,len(test_case)-1)
    median_test = test_case[median_index]

    test.assertEqual(correct_median,median_test,"Wrong median: {}".format(median_test)) 
    
    


if __name__ == '__main__':
    unittest.main()

