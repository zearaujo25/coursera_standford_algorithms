from closest_points import find_closest
from pair_of_points import PairOfPoints
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

class PairOfPointsTest(unittest.TestCase):
    def find_min_distance(self):
        point1 = Point(0,0)
        point2 = Point(0,5)
        point3 = Point(0,1)
        correct_pair = PairOfPoints(point1,point3)
        correct_distance = correct_pair.get_distance()


        result_pair = PairOfPoints.get_closest_pair([ PairOfPoints(point1,point2),
                                        PairOfPoints(point1,point3),
                                        PairOfPoints(point2,point3)])
        result_distance = result_pair.get_distance()

        self.assertEqual(correct_distance,result_distance) 
        self.assertEqual(correct_distance,result_pair.get_distance(),msg="Wrong points returned: {}".format(result_pair))
        returned_point1,returned_point2 =result_pair.get_closest_points()
        self.assertTrue(returned_point1 in correct_pair.get_points())
        self.assertTrue(returned_point2 in correct_pair.get_points())



if __name__ == '__main__':
    unittest.main()