"""
13.3 Dynamic Programming

Matrix Chain-Product problem

Description: Dynamic programming algorithm for the matrix
chain product problem
"""

def matrix_chain(d):
    """

    :param d: is a list of n+1 numbers such that size of kth
    matrix is d[k] by d[k+1]
    :return: n by n table such that N[i][j] represents min num
    of multiplications needed
    """

    n = len(d) - 1
    N = [[0] * n for i in range(n)]

    for b in range(1, n):        # num of products in subchain
        for i in range(n-b):    # start of subchain?
            j = i + b           # end of subchain
            N[i][j] = min(N[i][k] + N[k+1][j] + d[i]*d[k+1]*d[j+1]
                          for k in range(i, j))
            print("i, j:", i, j, N[i][j])
    return N

d = [2, 10, 50, 20]
print(matrix_chain(d))