import numpy as np
from methods.linearSystems.ElimGauss import ElimGauss

""" 
Resuelva Ios siguientes sistemas lineales usando método
de eliminación de Gauss
"""


class ExercisesUsingElimGauss:

    class ExerciseA:
        A = np.array([
            [3.333,     15920,      -10.333],
            [2.222,     16.710,     6.612],
            [1.5611,    5.1791,     1.6852]
        ])

        b = np.array([
            15913,
            28.544,
            8.4254
        ])

        def resolve(self,):
            print("Solución:", ElimGauss(self.A, self.b, proc=True))

    class ExerciseB:
        A = np.array([
            [1, 0.5, 0.33],
            [0.5, 0.33, 0.25],
            [0.33, 0.25, 0.2]
        ])

        b = np.array([
            2.0,
            1.0,
            0.0
        ])

        def resolve(self,):
            print("Solución:", ElimGauss(self.A, self.b))

    class ExerciseC:
        A = np.array([
            [1.0,   2.0,    -12.0,  8.0],
            [5.0,   4.0,    7.0,    -2.0],
            [-3.0,  7.0,    9.0,    5.0],
            [6.0,   -12.0,  -8.0,   3.0],
        ])

        b = np.array([
            27.0,
            4.0,
            11.0,
            49.0
        ])

        def resolve(self,):
            print("Solución:", ElimGauss(self.A, self.b, proc=True))
