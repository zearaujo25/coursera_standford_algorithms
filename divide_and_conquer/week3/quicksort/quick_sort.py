def quick_sort(array, left_end=None,right_end=None):
    if(left_end is None or right_end is None):
            left_end = 0
            right_end = len(array) -1
    if left_end >= right_end:
        return
    pivot_position = choose_pivot(array,left_end,right_end)
    swap(array,left_end,pivot_position)
    pivot_final_position = partition(array,left_end,right_end)
    quick_sort(array,left_end,pivot_final_position-1)
    quick_sort(array,pivot_final_position+1,right_end)

def choose_pivot(array,left_end,right_end):
    return left_end

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

def main():
    sorted_array = [0,1,2,3,4,5,6,7,8,9]
    array = [9,8,7,6,5,4,3,2,1,0]
    quick_sort(array)
    assert sorted_array == array , "Array not properly sorted: {}".format(array)


if __name__ == "__main__":
    main()