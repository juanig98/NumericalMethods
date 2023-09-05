import numpy as np

from U2SystemsOfLinearEquations.methods.Jacobi import Jacobi


class ExerciseUsingJacobi:
    class ExerciseA:
        A = np.array([
            [4.0,   0.24,  -0.08],
            [0.09,  3.0,   -0.15],
            [0.04,  -0.08,   4.0],
        ], float)

        b = np.array([
            8.0,
            9.0,
            20.0
        ], float)

        TOL = 0.01
        MAX = 5
        x0 = np.array([
            0.0,
            0.0,
            0.0
        ])

        def resolve(self,):
            print("Solución:",
                  Jacobi(self.A,
                         self.b,
                         self.x0,
                         self.TOL,
                         self.MAX))

    class ExerciseB:
        A = np.array([
            [10.0,   -1.0,  2.0,    0.0],
            [-1.0,  11.0,   -1.0,   3.0],
            [2.0,   -1.0,   10.0,   -1.0],
            [0.0,   3.0,    -1.0,   8.0],
        ], float)

        b = np.array([
            6.0,
            25.0,
            -11.0,
            15.0,
        ], float)

        TOL = 0.001
        MAX = 10
        x0 = np.array([
            0.0,
            0.0,
            0.0,
            0.0
        ])

        def resolve(self,):
            print("Solución:",
                  Jacobi(self.A,
                         self.b,
                         self.x0,
                         self.TOL,
                         self.MAX))
