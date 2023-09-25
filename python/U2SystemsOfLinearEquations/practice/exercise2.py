import numpy as np
from U2SystemsOfLinearEquations.methods.GaussJordan import GaussJordan

"""
Resolver los siguientes sistemas de ecuaciones mediante el 
método de Gauss-Jotdan
"""


class ExercisesUsingGaussJordan:

    class ExerciseA:
        A = np.array([
            [0.0,   2.0,    0.0,    1.0],
            [2.0,   2.0,    3.0,    2.0],
            [4.0,   -3.0,   0.0,    1.0],
            [6.0,   1.0,    -6.0,   -5.0],
        ])

        b = np.array([
            0.0,
            -2.0,
            -7.0,
            6.0
        ])

        def resolve(self,):
            print("Solución:", GaussJordan(self.A, self.b, proc=True))

    class ExerciseB:
        A = np.array([
            [1.0,   2.0,    -4.0],
            [2.0,   5.0,    2.0],
            [4.0,   1.0,    -1.0],
        ])

        b = np.array([
            11.0,
            3.0,
            6.0
        ])

        def resolve(self,):
            print("Solución:", GaussJordan(self.A, self.b, proc=True))
