from strassen import multiply,add_matrixes
from random import randrange

def main():
    test_add()
    test_multiply_identities()
    test_multiply_random_matrix_with_identity()
    test_multiply_fixed_input()
    print("ALL TESTS PASSED")

def test_add():
    print("TEST ADD START") 
    identity_size = 8
    identity = create_indentity(identity_size)
    result = add_matrixes(identity,identity)
    expected_result =  [[2 if i==j else 0 for j in range(0,identity_size) ] for i in range(0,identity_size) ]
    assert result == expected_result, "Wrong result-- Expected: {}, result: {}".format(expected_result,result)
    print("TEST ADD PASSED")

def test_multiply_identities():
    print("TEST MULTIPLY_IDENTITIES START") 
    identity_size = 8
    identity = create_indentity(identity_size)
    result = multiply(identity,identity)
    expected_result =  identity
    assert result == expected_result, "Wrong result-- Expected: {}, result: {}".format(expected_result,result)
    print("TEST MULTIPLY_IDENTITIES PASSED")

def test_multiply_random_matrix_with_identity():
    print("TEST MULTIPLY_RANDOM START") 
    matrix_size = 8
    identity = create_indentity(matrix_size)
    random_matrix = create_random_matrix(matrix_size)
    result = multiply(random_matrix,identity)
    expected_result =  random_matrix
    assert result == expected_result, "Wrong result-- Expected: {}, result: {}".format(expected_result,result)
    print("TEST MULTIPLY_RANDOM PASSED")


def test_multiply_fixed_input():
    print("TEST MULTIPLY_FIXED START") 
    matrix_x = [ 
               [1,2,3,4],
               [5,6,7,8],
               [9,10,11,12],
               [13,14,15,16] 
               ]
    matrix_y = [ [13,14,15,16],
               [9,10,11,12],
               [5,6,7,8],
               [1,2,3,4]              
                ]
    expected_result = [ [50,60,70,80],
                        [162,188,214,240],
                        [274,316,358,400],
                        [386,444,502,560]]   
    result = multiply(matrix_x,matrix_y)
    assert result == expected_result, "Wrong result-- Expected: {}, result: {}".format(expected_result,result)
    print("TEST MULTIPLY_FIXED PASSED")


def create_indentity(n):
    return [[1 if i==j else 0 for j in range(0,n) ] for i in range(0,n) ]

def create_random_matrix(n):
    return [[randrange(0,100) for j in range(0,n) ] for i in range(0,n) ]

if __name__ == '__main__':
    main()

