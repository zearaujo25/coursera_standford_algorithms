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
        return point1.find_distance_to_point(point2)

    def __str__(self):
     return "X: {}, Y: {}".format(self.x,self.y)
        
