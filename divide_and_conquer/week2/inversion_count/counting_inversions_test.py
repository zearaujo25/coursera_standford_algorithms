from counting_inversions import count_inversions

def main():
    worst_case_inversions()
    no_inversions()
    just_one_inversion()
    print("ALL TESTS PASSED")

def worst_case_inversions():
    unordered = '9876543210'
    ordered = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    correct_inversions = len(unordered)*(len(unordered)-1)/2
    result,inversions = count_inversions(unordered)
    assert (ordered == result and correct_inversions == inversions), "Wrong Sort: {}, Wrong Inversions: {}".format(result,inversions) 

def no_inversions():
    unordered = '0123456789'
    ordered = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    correct_inversions = 0
    result,inversions = count_inversions(unordered)
    assert (ordered == result and correct_inversions == inversions), "Wrong Sort: {}, Wrong Inversions: {}".format(result,inversions) 


def just_one_inversion():
    unordered = '0123456798'
    ordered = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    correct_inversions = 1
    result,inversions = count_inversions(unordered)
    assert (ordered == result and correct_inversions == inversions), "Wrong Sort: {}, Wrong Inversions: {}".format(result,inversions) 





if __name__ == '__main__':
    main()

