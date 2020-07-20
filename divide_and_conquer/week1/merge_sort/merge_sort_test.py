from merge_sort import merge_sort

def main():
    totally_unordered_test()
    ordered_test()
    partially_ordered_test()
    print("ALL TESTS PASSED")

def totally_unordered_test():
    unordered = '9876543210'
    ordered = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    result = merge_sort(unordered)
    assert merge_sort(unordered) == ordered, "Wrong result: {}".format(result)

def ordered_test():
    unordered = '0123456789'
    ordered = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    result = merge_sort(unordered)
    assert merge_sort(unordered) == ordered, "Wrong result: {}".format(result)

def partially_ordered_test():
    unordered = '5678901234'
    ordered = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    result = merge_sort(unordered)
    assert merge_sort(unordered) == ordered, "Wrong result: {}".format(result)


if __name__ == '__main__':
    main()

