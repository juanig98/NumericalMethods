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

    def resolve_with_Jacobi(self,):
        print("Solución:",
              Jacobi(self.A,
                     self.b,
                     self.x0,
                     self.TOL,
                     self.MAX))

    def resolve_with_GaussSeidel(self,):
        print("Solución:",
              GaussSeidel(self.A,
                          self.b,
                          self.x0,
                          self.TOL,
                          self.MAX))
