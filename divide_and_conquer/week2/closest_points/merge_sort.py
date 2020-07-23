from point import Point
def merge_sort(string_input,axis):
    string_size = len(string_input)
    if string_size == 1:
        return string_input
    
    sorted_left_half = merge_sort(string_input[:string_size//2],axis)
    sorted_right_half = merge_sort(string_input[string_size//2:],axis)

    return merge(sorted_left_half,sorted_right_half,axis)


def merge(sorted_left_half,sorted_right_half,axis):
    left_size = len(sorted_left_half)
    right_size = len(sorted_right_half)
    merge_size = left_size +  right_size
    merged_array = []
    left_index = 0
    right_index = 0
    for k in range(0,merge_size):
        if left_index == left_size:
            merged_array.append(sorted_right_half[right_index])
            right_index+=1
            continue

        elif right_index == right_size:
            merged_array.append(sorted_left_half[left_index])
            left_index+=1
            continue

        elif get_coordinate(sorted_left_half,left_index,axis) <= get_coordinate(sorted_right_half,right_index,axis):
            merged_array.append(sorted_left_half[left_index])
            left_index+=1
            continue

        elif get_coordinate(sorted_left_half,left_index,axis) > get_coordinate(sorted_right_half,right_index,axis):
            merged_array.append(sorted_right_half[right_index])
            right_index+=1
            continue
        else:
            raise Exception("Erro nao esperado")
        


    return merged_array

def get_coordinate(points,position,axis):
    return points[position].get_coordinates()[axis]


if __name__ == '__main__':
    correct = [Point(0,0), Point(1,0),Point(2,0) , Point(3,0), Point(4,0)]
    axis = 0
    unordered_input = list(reversed(correct))
    sorted_input = merge_sort(unordered_input,axis)
    assert correct == sorted_input, "Wrong Sort: {}".format(sorted_input) 

    correct = [Point(0,0), Point(0,1),Point(0,2) , Point(0,3), Point(0,4)]
    axis = 1
    unordered_input = list(reversed(correct))
    sorted_input = merge_sort(unordered_input,axis)
    assert correct == sorted_input, "Wrong Sort: {}".format(sorted_input) 



