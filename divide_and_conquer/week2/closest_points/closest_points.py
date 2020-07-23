from merge_sort import merge_sort
from point import Point

def pre_process(points):
    return merge_sort(points,0), merge_sort(points,1)



def find_closest(points = None,ordered_points_by_x=None,ordered_points_by_y=None):
    if points is not None:
        ordered_points_by_x,ordered_points_by_y = pre_process(points)
        return find_closest(ordered_points_by_x=ordered_points_by_x, ordered_points_by_y=ordered_points_by_y)
    

    


def main():
    pass

if __name__ == "__main__":
    main()