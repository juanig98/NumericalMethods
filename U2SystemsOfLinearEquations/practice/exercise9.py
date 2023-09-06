import numpy as np
from U2SystemsOfLinearEquations.methods.GaussSeidel import GaussSeidel
"""
Calcular una solución aproximada de los sistemas utilizando el método 
de Gauss-Seidel iterando hasta que se cumpla la condición de error
"""


class ExerciseUsingGaussSeidel:
    class ExerciseA:
        A = np.array([
            [1.0,   7.0,    -3.0],
            [4.0,   -4.0,   -9.0],
            [12.0,  -1.0,   3.0],
        ], float)

        b = np.array([
            51.0,
            61.0,
            8.0
        ], float)

        TOL = 0.001
        MAX = 6
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

    class ExerciseB:
        A = np.array([
            [3.0,   1.0,    1.0],
            [1.0,   5.0,    2.0],
            [1.0,   2.0,    5.0],
        ], float)

        b = np.array([
            10.0,
            21.0,
            30.0
        ], float)

        TOL = 0.001
        MAX = 7
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
