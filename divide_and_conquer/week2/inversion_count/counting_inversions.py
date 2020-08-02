def count_inversions(input_to_count):
    string_size = len(input_to_count)
    if string_size == 1:
        return input_to_count,0
    
    sorted_left_half,left_inversions = count_inversions(input_to_count[:string_size//2])
    sorted_right_half,right_inversions = count_inversions(input_to_count[string_size//2:])
    ordered_array,split_inversions = merge_and_count(sorted_left_half,sorted_right_half)
    inversions = left_inversions + right_inversions + split_inversions
    return ordered_array,inversions


def merge_and_count(sorted_left_half,sorted_right_half):
    left_size = len(sorted_left_half)
    right_size = len(sorted_right_half)
    merge_size = left_size +  right_size
    merged_array = []
    left_index = 0
    right_index = 0
    split_inversions = 0
    for k in range(0,merge_size):
        if left_index == left_size:
            merged_array.append(sorted_right_half[right_index])
            right_index+=1
            continue

        elif right_index == right_size:
            merged_array.append(sorted_left_half[left_index])
            left_index+=1
            continue

        elif sorted_left_half[left_index] <= sorted_right_half[right_index]:
            merged_array.append(sorted_left_half[left_index])
            left_index+=1
            continue

        elif sorted_left_half[left_index] > sorted_right_half[right_index]:
            merged_array.append(sorted_right_half[right_index])
            right_index+=1
            split_inversions+= left_size - left_index
            continue
        else:
            raise Exception("Erro nao esperado")
        


    return merged_array,split_inversions

    


def read_txt(path):
    test_case = []
    with open(path) as f: 
        for line in f: 
            test_case.append(int(line))
    return test_case


if __name__ == '__main__':
    correct_sort = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    correct_inversions = len(correct_sort)*(len(correct_sort)-1)/2
    string_input = '9876543210'
    sorted_input,inversions = count_inversions(string_input)
    assert (correct_sort == sorted_input and correct_inversions == inversions), "Wrong Sort: {}, Wrong Inversions: {}".format(sorted_input,inversions)
    assignment = read_txt("assignment.txt") 
    print(count_inversions(assignment)[1])


