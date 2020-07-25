from closest_points import find_closest
from point import Point
from random import randrange

import unittest

def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return float('.'.join([i, (d+'0'*n)[:n]]))

class PointTestCase(unittest.TestCase):
    def test_distance_only_y(self):
        poiint1 = Point(0,0)
        poiint2 = Point(0,5)
        correct_distance = 5
        result_distance = poiint1.find_distance_to_point(poiint2)
        self.assertEqual(correct_distance,result_distance) 

    def test_distance_only_x(self):
        poiint1 = Point(5,0)
        poiint2 = Point(0,0)
        correct_distance = 5
        result_distance = poiint1.find_distance_to_point(poiint2)
        self.assertEqual(correct_distance,result_distance) 
    
    def test_distance_both(self):
        poiint1 = Point(1,3)
        poiint2 = Point(2,4)
        correct_distance = 1.41421
        result_distance = poiint1.find_distance_to_point(poiint2)
        result_truncated = truncate(result_distance,5)
        self.assertEqual(correct_distance,result_truncated,msg="Resulted Wrong distance: {}".format(result_distance))


if __name__ == '__main__':
    unittest.main()