from math import *
from pprint import pprint


def distinf(x, y):
    """Implementación distancia dada por la norma infinito"""
    return max([abs(x[i]-y[i]) for i in range(len(x))])

def GaussSeidel(A, b, x0, TOL, MAX):
    """
    Implementación del método de Gauss-Seidel
    Entradas:
    A -- matriz cuadrada
    b -- vector
    x0 -- aproximación inicial
    TOL -- tolerancia
    MAX -- número máximo de iteraciones
    Salida:
    x -- aproximación a solución del sistema Ax = b
    None -- en caso de agotar las iteraciones o presentar errores
    """
    n = len(A)
    x = [0.0 for x in range(n)]
    k = 1
    while k <= MAX:  
        for i in range(n):
            if abs(A[i][i]) <= 1e-15:
                print("Imposible iterar")
                return None
            s1 = sum([A[i][j]*x[j] for j in range(i)])
            s2 = sum([A[i][j]*x0[j] for j in range(i+1, n)])
            x[i] = (b[i] - s1 - s2)/A[i][i]
        pprint(x)
        if distinf(x, x0) < TOL:
            print(r"Solución encontrada")
            return x
        k += 1
        for i in range(n):
            x0[i] = x[i]
    print("Iteraciones agotadas")
    return None

""" 
TESTING: 
A = [[2, 1], [5, 7]]
b = [11, 13]
x0 = [1, 1]
print("Matriz A:")
pprint(A)
print("Vector b:")
pprint(b)
print("Semilla x0:")
pprint(x0)
print("Iteración de Gauss-Seidel")
# T OL = 10−5, MAX = 50
GaussSeidel(A, b, x0, 1e-5, 50)

A = [[10, -1, 2], [-1, 11, -1], [2, -1, 10]]
b = [6, 25, -11]
x0 = [0, 0, 0]
print("Matriz A:")
pprint(A)
print("Vector b:")
pprint(b)
print("Semilla x0:")
pprint(x0)
print("Iteración de Gauss-Seidel")
# T OL = 10−10, MAX = 50
GaussSeidel(A, b, x0, 1e-10, 50)
"""