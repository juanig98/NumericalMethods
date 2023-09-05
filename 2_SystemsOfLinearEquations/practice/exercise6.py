import numpy as np
from methods.linearSystems.ElimGauss import ElimGauss

from methods.linearSystems.GaussJordan import GaussJordan

""" 
Hallar la solución de los siguientes sistemas tridiagonales
"""


class ExerciseTridiagonalSystems:
    class ExerciseA:

        A = np.array([
            [2.0,    -1.0,    0.0,    0.0],
            [-1.0,   2.0,    -1.0,   0.0],
            [0.0,    -1.0,   2.0,    -1.0],
            [0.0,    0.0,    -1.0,    2.0],
        ])

        B = np.array([
            1.0,
            0.0,
            0.0,
            1.0,
        ])

        def resolve(self,):
            print("Solución (usando Eliminación de Gauss):",
                  ElimGauss(self.A, self.B, proc=True))

            print("Solución (usando Gauss-Jordan):",
                  GaussJordan(self.A, self.B, proc=True))

    class ExerciseB:
        A = np.array([
            [0.5,    0.25,   0.0,   0.0],
            [0.35,   0.8,    0.4,   0.0],
            [0.0,    0.25,   1.0,   0.5],
            [0.0,    0.0,    1.0,   -2.0],
        ])

        B = np.array([
            0.35,
            0.77,
            -0.5,
            -2.25,
        ])

        def resolve(self,):
            print("Solución (usando Eliminación de Gauss):",
                  ElimGauss(self.A, self.B, proc=True))

            print("Solución (usando Gauss-Jordan):",
                  GaussJordan(self.A, self.B, proc=True))
