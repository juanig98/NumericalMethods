import numpy as np

from methods.linearSystems.ElimGauss import ElimGauss
from methods.linearSystems.GaussJordan import GaussJordan


class Exercise1:

    def a():
        A = np.array([
            [3.333, 15920, -10.333],
            [2.222, 16.710, 6.612],
            [1.5611, 5.1791, 1.6852]
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
            [1.0, 2.0, -12.0, 8.0],
            [5.0, 4.0, 7.0, -2.0],
            [-3.0, 7.0, 9.0, 5.0],
            [6.0, -12.0, -8.0, 3.0],
        ])

        b = np.array([27.0, 4.0, 11.0, 49.0])

        print("Solución:", ElimGauss(A, b, proc=True))


class Exercise2:

    def a():
        A = np.array([
            [0.0, 2.0, 0.0, 1.0],
            [2.0, 2.0, 3.0, 2.0],
            [4.0, -3.0, 0.0, 1.0],
            [6.0, 1.0, -6.0, -5.0],
        ])

        b = np.array([0.0, -2.0, -7.0, 6.0])

        print("Solución:", GaussJordan(A, b))

    def b():
        A = np.array([
            [1.0, 2.0, -4.0],
            [2.0, 5.0, 2.0],
            [4.0, 1.0, -1.0],
        ])

        b = np.array([11.0, 3.0, 6.0])

        print("Solución:", GaussJordan(A, b))
