from math import sqrt  
from point import Point

class PointPair:
    '''A class that represent a pair of points in a plane'''
    def __init__(self,point1,point2):
        self.p1 = point1
        self.p2 = point2

    def get_points(self):
        return self.p1,self.p2

    def get_distance(self):
        return self.p1.find_distance_to_point(self.p2)

    @staticmethod   
    def get_closest_pair(pair_list):
        min_distance = float("inf")
        min_pair = None
        for pair in pair_list:
            if pair is None:
                continue
            if pair.get_distance() < min_distance:
                min_pair = pair
        return min_pair
