from closest_points import find_closest
from point import Point
from pair_of_points import PairOfPoints
from random import randrange,seed,shuffle
seed(42)

import unittest

def broken_function():
    raise Exception('This is broken')

def create_test_case(correct_pair,n):
    random_base = randrange(start=20)
    point1,point2 = correct_pair.get_points()
    test_case = [Point(randrange(0,100),i) for i in range(random_base,random_base+n*2,2)]
    test_case.append(point2)
    test_case.insert(0,point1)
    shuffle(test_case)
    return test_case

class ClosestPointTest(unittest.TestCase):
    def test_one_point(self):
        points = [Point(0,0)]
        with self.assertRaises(Exception) as context:
            find_closest(points)
        self.assertTrue("Single point to find value" in str(context.exception)) 

    def test_two_points(self):
        points = [Point(0,0),Point(0,5)]
        correct_distance = points[0].find_distance_to_point(points[1])
        closest_pair = find_closest(points)
        self.assertEqual(correct_distance,closest_pair.get_distance())

    def test_three_points(self):
        correct_pair = PairOfPoints(Point(0,0),Point(0,1))
        points = [correct_pair.p1,Point(0,5),correct_pair.p2]
        correct_distance = correct_pair.get_distance()
        result_pair = find_closest(points)
        self.assertEqual(correct_distance,result_pair.get_distance(),msg="Wrong points returned: {}".format(result_pair))
        returned_point1,returned_point2 =result_pair.get_points()
        self.assertTrue(returned_point1 in correct_pair.get_points())
        self.assertTrue(returned_point2 in correct_pair.get_points())

    def test_four_points(self):
        correct_pair = PairOfPoints(Point(0,0),Point(0,1))
        points = [correct_pair.p1,Point(0,5),correct_pair.p2,Point(23,4)]
        correct_distance = correct_pair.get_distance()
        result_pair = find_closest(points)
        self.assertEqual(correct_distance,result_pair.get_distance(),msg="Wrong points returned: {}".format(result_pair))
        returned_point1,returned_point2 =result_pair.get_points()
        self.assertTrue(returned_point1 in correct_pair.get_points())
        self.assertTrue(returned_point2 in correct_pair.get_points())

    def test_best_points_right(self):
        correct_pair = PairOfPoints(Point(0,0),Point(0,1))
        points = create_test_case(correct_pair,10000)
        correct_distance = correct_pair.get_distance()
        result_pair = find_closest(points)
        self.assertEqual(correct_distance,result_pair.get_distance(),msg="Wrong points returned: {}".format(result_pair))
        returned_point1,returned_point2 =result_pair.get_points()
        self.assertTrue(returned_point1 in correct_pair.get_points())
        self.assertTrue(returned_point2 in correct_pair.get_points())

    def test_best_points_left(self):
        correct_pair = PairOfPoints(Point(1000000,0),Point(1000000,1))
        points = create_test_case(correct_pair,10000)
        correct_distance = correct_pair.get_distance()
        result_pair = find_closest(points)
        self.assertEqual(correct_distance,result_pair.get_distance(),msg="Wrong points returned: {}".format(result_pair))
        returned_point1,returned_point2 =result_pair.get_points()
        self.assertTrue(returned_point1 in correct_pair.get_points(),msg="Wrong pair: {}".format(result_pair))
        self.assertTrue(returned_point2 in correct_pair.get_points())

if __name__ == '__main__':
    unittest.main()