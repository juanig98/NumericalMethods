import numpy as np
from methods.linearSystems.ElimGauss import ElimGauss

""" 
Aplicar el método de Gauss con pivoteo parcial.
"""


class ExerciseUsingGaussWithPartialPivot:
    A = np.array([
        [-1.41,     2.0,        0.0],
        [1.0,       -1.41,      1.0],
        [0.0,       2.0,        -1.41],
    ])

    b = np.array([
        1.0,
        1.0,
        1.0
    ])

    def resolve(self,):
        print("Solución:", ElimGauss(self.A, self.b, proc=True))
