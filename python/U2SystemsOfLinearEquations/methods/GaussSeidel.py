from math import *
from pprint import pprint
import numpy as np


def GaussSeidel(A, b, x0, TOL, max_iterations, proc=False):
    n = len(A)
    x = x0.copy()

    # Gauss-Seidal Method [By Bottom Science]

    for i in range(max_iterations):
        x_new = np.zeros(n)
        for j in range(n):
            s1 = np.dot(A[j, :j], x_new[:j])
            s2 = np.dot(A[j, j + 1:], x[j + 1:])
            x_new[j] = (b[j] - s1 - s2) / A[j, j]
        d = np.linalg.norm(np.array(x_new)-np.array(x), np.inf)
        if proc:
            print("\nIteración {}: \t{} \tError: {}"
                  .format(i+1, x_new, d))
        if abs(d) < abs(TOL):
            print("\nSe superó la tolerancia máxima!\nEl error es de {} menor a la tolerancia de {}\n"
                  .format(abs(d), abs(TOL)))
            return x_new
        # if np.allclose(x, x_new, rtol=TOL):
        #     print("\nSe superó la tolerancia máxima!\nEl error es de {} menor a la tolerancia de {}\n"
        #           .format(abs(d), abs(TOL)))
        #     return x_new
        x = x_new
    return x


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
