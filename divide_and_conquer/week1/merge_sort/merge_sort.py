def merge_sort(string_input):
    string_size = len(string_input)
    if string_size == 1:
        return string_input
    
    sorted_left_half = merge_sort(string_input[:string_size//2])
    sorted_right_half = merge_sort(string_input[string_size//2:])

    return merge(sorted_left_half,sorted_right_half)


def merge(sorted_left_half,sorted_right_half):
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

        elif sorted_left_half[left_index] <= sorted_right_half[right_index]:
            merged_array.append(sorted_left_half[left_index])
            left_index+=1
            continue

        elif sorted_left_half[left_index] > sorted_right_half[right_index]:
            merged_array.append(sorted_right_half[right_index])
            right_index+=1
            continue
        else:
            raise Exception("Erro nao esperado")
        


    return merged_array

    




if __name__ == '__main__':
    correct = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    string_input = '9876543210'
    sorted_input = merge_sort(string_input)
    assert correct == sorted_input, "Wrong Sort: {}".format(sorted_input) 


