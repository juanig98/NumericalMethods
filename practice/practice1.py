import numpy as np

from methods.linearSystems.ElimGauss import ElimGauss
from methods.linearSystems.GaussJordan import GaussJordan
from methods.linearSystems.GaussSeidel import GaussSeidel
from methods.linearSystems.Jacobi import Jacobi
from methods.linearSystems.LU import LU


class Exercise1:

    def a():
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

        print("Solución:", ElimGauss(A, b, proc=True))

    def b():
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

        print("Solución:", ElimGauss(A, b))

    def c():
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

        print("Solución:", ElimGauss(A, b, proc=True))


class Exercise2:

    def a():
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

        print("Solución:", GaussJordan(A, b, proc=True))

    def b():
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

        print("Solución:", GaussJordan(A, b, proc=True))


class Exercise3:

    def a():
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

        print("Solución:", ElimGauss(A, b, proc=True))


class Exercise4:

    def resolve():
        A = np.array([
            [20.0,  25.0,   40.0,   50.0],
            [10.0,  15.0,   20.0,   22.0],
            [10.0,  8.0,    10.0,   15.0],
            [3.0,   4.0,    7.0,    20.0],
        ])

        b = np.array([
            1970.0,
            970.0,
            601.0,
            504.0
        ])

        print("Solución:", ElimGauss(A, b, proc=True))


class Exercise5:

    def a():

        A = np.array([
            [4.0,   -2.0,   -1.0],
            [5.0,   1.0,    -1.0],
            [1.0,   2.0,    -4.0]
        ])

        L, U = LU(A)

        print(L)
        print(U)
        # A = np.array([
        #     [2.0,  -1.0,    1.0],
        #     [3.0,  3.0,     16.5],
        #     [3.0,  3.0,     12.5],
        # ])

        # b = np.array([
        #     1970.0,
        #     970.0,
        #     601.0,
        #     504.0
        # ])

        # print("Solución:", LU(A))


class Exercise6:
    exe_a_A = np.array([
        [2.0,    -1.0,    0.0,    0.0],
        [-1.0,   2.0,    -1.0,   0.0],
        [0.0,    -1.0,   2.0,    -1.0],
        [0.0,    0.0,    -1.0,    2.0],
    ])

    exe_a_B = np.array([
        1.0,
        0.0,
        0.0,
        1.0,
    ])

    def a_with_elimgauss():
        print("Solución:", ElimGauss(
            Exercise6.exe_a_A,
            Exercise6.exe_a_B,
            proc=True)
        )

    def a_with_gaussjordan():
        print("Solución:", GaussJordan(
            Exercise6.exe_a_A,
            Exercise6.exe_a_B,
            proc=True)
        )

    exe_b_A = np.array([
        [0.5,    0.25,   0.0,   0.0],
        [0.35,   0.8,    0.4,   0.0],
        [0.0,    0.25,   1.0,   0.5],
        [0.0,    0.0,    1.0,   -2.0],
    ])

    exe_b_B = np.array([
        0.35,
        0.77,
        -0.5,
        -2.25,
    ])

    def b_with_elimgauss():
        print("Solución:", ElimGauss(
            Exercise6.exe_b_A,
            Exercise6.exe_b_B,
            proc=True)
        )

    def b_with_gaussjordan():
        print("Solución:", GaussJordan(
            Exercise6.exe_b_A,
            Exercise6.exe_b_B,
            proc=True)
        )


class Exercise7:

    def resolve():
        pass


class Exercise8:

    def a():
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
        x0 = np.array([0.0, 0.0, 0.0])
        print("Solución:", Jacobi(A, b, x0, TOL, MAX))

    def b():
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
        x0 = np.array([0.0, 0.0, 0.0, 0.0])
        print("Solución:", Jacobi(A, b, x0, TOL, MAX))


class Exercise9:
    def a():
        pass


class Exercise10:
    pass
