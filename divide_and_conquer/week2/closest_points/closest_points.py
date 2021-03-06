from merge_sort import merge_sort
from point import Point
from pair_of_points import PairOfPoints
def pre_process(points):
    return merge_sort(points,0), merge_sort(points,1)

def find_closest(points = None,ordered_points_by_x=None,ordered_points_by_y=None):
    #remeber, they are the same set of points ordered by differetn criteria

    if points is not None:
        ordered_points_by_x,ordered_points_by_y = pre_process(points)
        return find_closest(ordered_points_by_x=ordered_points_by_x, ordered_points_by_y=ordered_points_by_y)
    
    size = len(ordered_points_by_x)
    if size <=3:
        return base_case(ordered_points_by_x)
    
    Lx,Rx = split_x(ordered_points_by_x,size)
    x_median = ordered_points_by_x[size//2-1].x
    Ly, Ry = split_y(ordered_points_by_y, x_median)


    best_left = find_closest(ordered_points_by_x= Lx, ordered_points_by_y= Ly)
    best_right = find_closest(ordered_points_by_x= Rx, ordered_points_by_y= Ry)
    best_pair = PairOfPoints.get_closest_pair((best_left,best_right))

    delta = best_pair.get_distance()
    best_split = closest_split(ordered_points_by_x,ordered_points_by_y,delta)

    return PairOfPoints.get_closest_pair((best_pair,best_split))


def base_case(points):
    point1 = points[0]
    if len(points) == 1:
        raise Exception("Single point to find value")
    point2 = points[1]
    if len(points) == 2:
        return PairOfPoints(point1,point2)
    point3 = points[2]
    return PairOfPoints.get_closest_pair([ PairOfPoints(point1,point2),
                                        PairOfPoints(point1,point3),
                                        PairOfPoints(point2,point3)])

def split_x(points,size):
    return points[:size//2],points[size//2:]

def split_y(ordered_points_by_y, x_median):
    Ly,Ry = [],[]
    for point in ordered_points_by_y:
        if point.x <= x_median:
            Ly.append(point)
        else:
            Ry.append(point)
    return Ly, Ry

def closest_split(ordered_points_by_x,ordered_points_by_y,delta):
    size = len(ordered_points_by_x)
    x_bar = ordered_points_by_x[size//2 -1].x #median
    upper_x = x_bar + delta
    lower_x = x_bar - delta
    Sy = [point  for point in ordered_points_by_y if point.x >=lower_x and point.x<= upper_x]
    s_size = len(Sy)
    if s_size <=1:
        return None

    best = delta
    best_pair = None

    for i in range(0,s_size):
        for j in range(1,min(7,s_size-i)):
            pq = PairOfPoints(Sy[i],Sy[i+j])
            if pq.get_distance() < best:
                best = pq.get_distance()
                best_pair = pq
    return best_pair

def main():
    pass

if __name__ == "__main__":
    main()