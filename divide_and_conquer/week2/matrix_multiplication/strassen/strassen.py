def multiply(matrix_X,matrix_Y):

    n = len(matrix_X)

    if n ==1:
        return [[matrix_X[0][0] * matrix_Y[0][0]]]

    A,B,C,D = split_matrix(matrix_X)
    E,F,G,H = split_matrix(matrix_Y)
    
    P1 = multiply(A,subtract_matrixes(F,H))
    P2 = multiply(add_matrixes(A,B),H)
    P3 = multiply(add_matrixes(C,D),E)
    P4 = multiply(D,subtract_matrixes(G,E))
    P5 = multiply(add_matrixes(A,D),add_matrixes(E,H))
    P6 = multiply(subtract_matrixes(B,D),add_matrixes(G,H))
    P7 = multiply(subtract_matrixes(A,C),add_matrixes(E,F))

    top_left = add_matrixes(P5,P4)
    top_left = subtract_matrixes(top_left,P2)
    top_left = add_matrixes(top_left,P6)

    top_right = add_matrixes(P1,P2)

    bottom_left = add_matrixes(P3,P4)

    bottom_right = add_matrixes(P1,P5)
    bottom_right = subtract_matrixes(bottom_right,P3)
    bottom_right = subtract_matrixes(bottom_right,P7)

    return merge_matrixes(n, top_left, top_right, bottom_left, bottom_right)

def merge_matrixes(n, top_left, top_right, bottom_left, bottom_right):
    
    result = [[0 for j in range(0, n)] for i in range(0, n)]
    
    for row in range(0,n//2):
        for column in range(0,n//2):
            result[row][column] = top_left[row][column]


    for row in range(0,n//2):
        for column in range(n//2,n):
            result[row][column] = top_right[row][column-n//2]


    for row in range(n//2,n):
        for column in range(0,n//2):
            result[row][column] = bottom_left[row-n//2][column]

    for row in range(n//2,n):
        for column in range(n//2,n):
            result[row][column] = bottom_right[row-n//2][column-n//2]
    
    return result

def split_matrix(matrix_X):
    
    n = len(matrix_X)
    
    A = [column[:n//2] for column in matrix_X[:n//2]]
    B = [column[n//2:] for column in matrix_X[:n//2]]
    C = [column[:n//2] for column in matrix_X[n//2:]]
    D = [column[n//2:] for column in matrix_X[n//2:]]
    
    return A,B,C,D


def add_matrixes(matrix_X,matrix_Y):
    return [[matrix_X[i][j] + matrix_Y[i][j]  for j in range(len(matrix_X[0]))] for i in range(len(matrix_Y))]
    
def subtract_matrixes(matrix_X,matrix_Y):
    return [[matrix_X[i][j] - matrix_Y[i][j]  for j in range(len(matrix_X[0]))] for i in range(len(matrix_Y))]
    
def create_indentity(n):
    return [[1 if i==j else 0 for j in range(0,n) ] for i in range(0,n) ]


if __name__ == '__main__':
    identity = create_indentity(2)
    result = multiply(identity,identity)
    assert result == identity , "Wrong multiplication: {}".format(result) 


