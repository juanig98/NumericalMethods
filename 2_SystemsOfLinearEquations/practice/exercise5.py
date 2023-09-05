import numpy as np

from methods.linearSystems.LU import LU

""" 
Aplicar el método de factorización para enconÍar solución
a los siguientes sistemas.
"""


class ExerciseUsingFactorizationLU:

    class ExerciseA:
        A = np.array([
            [4.0,   -2.0,   -1.0],
            [5.0,   1.0,    -1.0],
            [1.0,   2.0,    -4.0]
        ])

        def resolve(self,):
            L, U = LU(self.A)
            print("Solución: L={}, U={}".format(L, U))

    class ExerciseB:
        def resolve():
            pass
