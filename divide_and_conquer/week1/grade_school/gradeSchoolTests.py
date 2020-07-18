from gradeSchoolAlgorithm import multiply

def main():
    test_small_number()
    test_big_number()
    test_assignment()
    print("ALL TESTS PASSED")

def test_small_number():
    integer1 = '1234'
    integer2 = '1234'
    expected_result = 1522756
    assert multiply(integer1,integer2) == expected_result, "Wrong result"

def test_big_number():
    integer1 = '999999'
    integer2 = '999999'
    expected_result = 999998000001
    result = multiply(integer1,integer2)
    assert result == expected_result, "Wrong result: {}".format(result)

def test_assignment():
    integer1 = '3141592653589793238462643383279502884197169399375105820974944592'
    integer2 = '2718281828459045235360287471352662497757247093699959574966967627'
    expected_result = 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
    result = multiply(integer1,integer2)
    assert result == expected_result, "Wrong result: {}".format(result)


if __name__ == '__main__':
    main()

