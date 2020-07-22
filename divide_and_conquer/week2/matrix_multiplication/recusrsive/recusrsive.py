def multiply(matrix_X,matrix_Y):

    n = len(matrix_X)

    if n ==1:
        return [[matrix_X[0][0] * matrix_Y[0][0]]]
    
    result = [[0 for j in range(0, n)] for i in range(0, n)]

    A,B,C,D = split_matrix(matrix_X)
    E,F,G,H = split_matrix(matrix_Y)
    
    AE = multiply(A,E)
    BG = multiply(B,G)
    AF = multiply(A,F)
    BH = multiply(B,H)
    CE = multiply(C,E)
    DG = multiply(D,G)
    CF = multiply(C,F)
    DH = multiply(D,H)

    AE_BG = add_matrixes(AE,BG)
    AF_BH = add_matrixes(AF,BH)
    CE_DG = add_matrixes(CE,DG)
    CF_DH = add_matrixes(CF,DH)

    for row in range(0,n//2):
        for column in range(0,n//2):
            result[row][column] = AE_BG[row][column]
            
    
    for row in range(0,n//2):
        for column in range(n//2,n):
            result[row][column] = AF_BH[row][column-n//2]

    
    for row in range(n//2,n):
        for column in range(0,n//2):
            result[row][column] = CE_DG[row-n//2][column]

    for row in range(n//2,n):
        for column in range(n//2,n):
            result[row][column] = CF_DH[row-n//2][column-n//2]

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
    


def create_indentity(n):
    return [[1 if i==j else 0 for j in range(0,n) ] for i in range(0,n) ]


if __name__ == '__main__':
    identity = create_indentity(2)
    result = multiply(identity,identity)
    assert result == identity , "Wrong multiplication: {}".format(result) 


