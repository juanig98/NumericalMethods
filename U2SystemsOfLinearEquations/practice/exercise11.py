import numpy as np

from U2SystemsOfLinearEquations.methods.GaussSeidel import GaussSeidel

"""
Aplique la iteración de Gauss-seidel al sistema. Comience con la aproximación xu=O para todo k, e itele hasta que se
cumpla
"""


class ExerciseUsingGaussSeidel2:
    A = np.array([
        [-2.0,  1.0,    0.0,    0.0],
        [1.0,   -2.0,   1.0,    0.0],
        [0.0,   1.0,    -2.0,   1.0],
        [0.0,   0.0,    1.0,    -2.0],
    ], float)

    b = np.array([
        -1.0,
        0.0,
        0.0,
        0.0
    ], float)

    TOL = 0.001
    MAX = 10
    x0 = np.array([
        0.0,
        0.0,
        0.0
    ])

    def resolve(self,):
        print("Solución:",
              GaussSeidel(self.A,
                          self.b,
                          self.x0,
                          self.TOL,
                          self.MAX))
