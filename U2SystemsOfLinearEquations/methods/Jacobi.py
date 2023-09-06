from math import *
from pprint import pprint
import numpy as np


def jacobi(a, b, x):
    n = len(x)
    t = x.copy()
    for i in range(n):
        s = 0
        for j in range(n):
            if i != j:
                s = s+a[i, j]*t[j]
                x[i] = (b[i]-s)/a[i, i]
    return x


def Jacobi(A, b, x0, TOL, MAX):
    """
    Implementación del método de Jacobi
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
    # n = len(x0)
    t = x0.copy()
    for k in range(MAX):
        x0 = jacobi(A, b, x0)
        d = np.linalg.norm(np.array(x0)-np.array(t), np.inf)
        print("\nIteración {}: \t{} \tError: {}"
              .format(k+1, str(np.transpose(x0.round(7))), abs(d)))
        if abs(d) < abs(TOL):
            print("\nSe superó la tolerancia máxima!\nEl error es de {} menor a la tolerancia de {}\n"
                  .format(abs(d), abs(TOL)))
            return [x0, k]
        else:
            t = x0.copy()
    return [[], MAX]


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
print("Iteración de Jacobi")
# T OL = 10−5, MAX = 50
Jacobi(A, b, x0, 1e-5, 50)

A = [[10, -1, 2], [-1, 11, -1], [2, -1, 10]]
b = [6, 25, -11]
x0 = [0, 0, 0]
print("Matriz A:")
pprint(A)
print("Vector b:")
pprint(b)
print("Semilla x0:")
pprint(x0)
print("Iteración de Jacobi")
# T OL = 10−10, MAX = 50
Jacobi(A, b, x0, 1e-10, 50)

"""
