from recursiveMultiplication import multiply_recursively

def main():
    test_small_number()
    test_big_number_9()
    test_assignment()
    print("ALL TESTS PASSED")

def test_small_number():
    print("TEST START")
    integer1 = '1234'
    integer2 = '5678'
    expected_result = 7006652
    result = multiply_recursively(integer1,integer2)
    assert result == expected_result, "Wrong result-- Expected: {}, result: {}".format(expected_result,result)

def test_big_number_9():
    print("TEST START")
    integer1 = '99999999'
    integer2 = '99999999'
    expected_result = 9999999800000001
    result = multiply_recursively(integer1,integer2)
    assert result == expected_result, "Wrong result-- Expected: {}, result: {}".format(expected_result,result)



def test_assignment():
    print("TEST START")
    integer1 = '3141592653589793238462643383279502884197169399375105820974944592'
    integer2 = '2718281828459045235360287471352662497757247093699959574966967627'
    expected_result = 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
    result = multiply_recursively(integer1,integer2)
    assert result == expected_result, "Wrong result-- Expected: {}, result: {}".format(expected_result,result)


if __name__ == '__main__':
    main()

