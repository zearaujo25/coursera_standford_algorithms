def quick_sort(array, left_end=None, right_end=None, pivot_method='naive_begin' ):
    
    if(left_end is None or right_end is None):
            left_end = 0
            right_end = len(array) -1
    number_of_comparisons = get_number_of_comparisons(array,left_end,right_end)
    if left_end >= right_end:
        return number_of_comparisons

    pivot_position = get_pivot(pivot_method, array, left_end, right_end)
    swap(array,left_end,pivot_position)
    
    pivot_final_position = partition(array,left_end,right_end)
    
    number_of_comparisons = get_number_of_comparisons(array,left_end,right_end)
    left = quick_sort(array,left_end,pivot_final_position-1,pivot_method=pivot_method)
    right = quick_sort(array,pivot_final_position+1,right_end,pivot_method)
    return left + right + number_of_comparisons

def get_pivot(pivot_method, array, left_end, right_end):

    if pivot_method == 'naive_begin':
        return choose_pivot_naive_begin(array,left_end,right_end)
    elif pivot_method == 'naive_end':
        return choose_pivot_naive_end(array,left_end,right_end)
    elif pivot_method == 'median': 
        return  choose_pivot_median(array,left_end,right_end)
    else:
        raise Exception("Wrong pivot method")

def choose_pivot_naive_begin(array,left_end,right_end):
    return left_end

def choose_pivot_naive_end(array,left_end,right_end):
    return right_end

def choose_pivot_median(array,left_end,right_end):
    middle = left_end + ((right_end-left_end)//2) 
    aux_array = [array[left_end],array[middle],array[right_end]]
    aux_array.sort()
    median = aux_array[1]
    if median == array[left_end]:
        return left_end
    elif median == array[right_end]:
        return right_end
    else:
        return middle

def partition(array,left_end,right_end):
    pivot = array[left_end]
    i = left_end+1
    for j in range(left_end+1,right_end+1):
        if array[j]<pivot:
            swap(array,i,j)
            i += 1 
    
    swap(array,left_end,i-1)
    #final place of the pivot 
    return i-1

def swap(array,i,j):
    array[i],array[j] = array[j],array[i]

def get_number_of_comparisons(array,left_end,right_end):
    return  len(array[left_end:right_end]) if left_end < right_end else 0

#Assignment code
def read_txt(path):
    test_case = []
    with open(path) as f: 
        for line in f: 
            test_case.append(int(line))
    return test_case

def main():
    assignment = read_txt("assignment.txt")
    # print("Assignment naive begin: {}".format(quick_sort(assignment,pivot_method="naive_begin")))
    # print("Assignment naive end: {}".format(quick_sort(assignment,pivot_method="naive_end")))
    print("Assignment naive median: {}".format(quick_sort(assignment,pivot_method="median")))

if __name__ == "__main__":
    main()