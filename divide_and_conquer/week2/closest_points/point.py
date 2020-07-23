from math import sqrt  

class Point:
    '''A class that represent a point in a plane'''
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return self.x,self.y

    def find_distance_to_point(self,point):
        x,y = point.get_coordinates()
        return sqrt( (self.x - x )**2 + (self.y-y)**2  )

    @staticmethod
    def find_distance(point1,point2):
        x1,y1 = point1.get_coordinates()
        x2,y2 = point2.get_coordinates()
        return sqrt( (x1 - x2)**2 + (y1 - y2)**2  )
