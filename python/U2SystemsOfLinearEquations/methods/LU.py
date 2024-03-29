from math import *
from pprint import pprint


def LU(A, proc=False):
    """
    Implementación del método LU
    Entradas:
    A -- matriz cuadrada
    Salidas:
    L, U -- matrices de la descomposición
    None -- en caso de no ser posible la descomposición
    """
    n = len(A)
    # crear matrices nulas
    L = [[0 for x in range(n)] for x in range(n)]
    U = [[0 for x in range(n)] for x in range(n)]
    # Doolittle
    L[0][0] = 1
    U[0][0] = A[0][0]

    if abs(L[0][0]*U[0][0]) <= 1e-15:
        print("Imposible descomponer")
        return None

    for j in range(1, n):
        U[0][j] = A[0][j]/L[0][0]
        L[j][0] = A[j][0]/U[0][0]

    for i in range(1, n-1):
        L[i][i] = 1
        s = sum([L[i][k]*U[k][i] for k in range(i)])
        U[i][i] = A[i][i] - s

    if abs(L[i][i]*U[i][i]) <= 1e-15:
        print("Imposible descomponer")
        return None

    for j in range(i+1, n):
        s1 = sum([L[i][k]*U[k][j] for k in range(i)])
        s2 = sum([L[j][k]*U[k][i] for k in range(i)])
        U[i][j] = A[i][j] - s1
        L[j][i] = (A[j][i] - s2)/U[i][i]

    L[n-1][n-1] = 1.0
    s3 = sum([L[n-1][k]*U[k][n-1] for k in range(n)])
    U[n-1][n-1] = A[n-1][n-1] - s3

    if abs(L[n-1][n-1]*U[n-1][n-1]) <= 1e-15:
        print("Imposible descomponer")
        return None

    if proc:
        print("Matriz L:")
        pprint(L)
        print("Matriz U:")
        pprint(U)
    return L, U


""" 
TESTING: 
A = [[4, 3], [6, 3]]
print("Matriz A:")
pprint(A)
lu(A)

A = [[0, 1], [1, 1]]
print("Matriz A:")
pprint(A)
lu(A)

A = [[3, 1, 6], [-6, 0, -16], [0, 8, -17]]
print("Matriz A:")
pprint(A)
lu(A)

A = [[1, 2, 3], [2, 4, 5], [1, 3, 4]]
print("Matriz A:")
pprint(A)
lu(A) 
"""
