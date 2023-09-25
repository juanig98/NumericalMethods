import numpy as np
from U2SystemsOfLinearEquations.methods.GaussSeidel import GaussSeidel
from U2SystemsOfLinearEquations.methods.Jacobi import Jacobi

"""
Aplical los métodos itelativos (Jacobi y Seidel) para resolver 
el siguiente sistema e iterar hasta que se cumpla
"""


class ExerciseUsingIterativeMethods:
    A = np.array([
        [7.0,   -1.0,   4.0],
        [3.0,   -8.0,   2.0],
        [4.0,   1.0,    -6.0],
    ], float)

    b = np.array([
        8.0,
        -4.0,
        3.0
    ], float)

    TOL = 0.001
    MAX = 15
    x0 = np.array([
        0.0,
        0.0,
        0.0
    ])

    class UsingJacobi:
        def resolve(self,):
            print("Aplicando método de Jacobi")
            print("Solución",
                  Jacobi(ExerciseUsingIterativeMethods.A,
                         ExerciseUsingIterativeMethods.b,
                         ExerciseUsingIterativeMethods.x0,
                         ExerciseUsingIterativeMethods.TOL,
                         ExerciseUsingIterativeMethods.MAX,
                         ))

    class UsingGaussSeidel:
        def resolve(self,):
            print("Aplicando método de GaussSeidel")
            print("Solución:",
                  GaussSeidel(ExerciseUsingIterativeMethods.A,
                              ExerciseUsingIterativeMethods.b,
                              ExerciseUsingIterativeMethods.x0,
                              ExerciseUsingIterativeMethods.TOL,
                              ExerciseUsingIterativeMethods.MAX,
                              proc=True))
