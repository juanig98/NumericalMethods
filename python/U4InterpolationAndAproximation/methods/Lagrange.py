from math import *


def LagrangePol(datos):
    """
    Implementación del interpolador de Lagrange
    Entradas:
    datos -- lista de puntos (x, y) en el plano
    Salida:
    P -- función de interpolación
    """

    def L(k, x):
        """Implementación funciones L_k(x)"""

        out = 1
        for i, p in enumerate(datos):
            if i != k:
                out *= (x - p[0])/(datos[k][0] - p[0])
        return out

    def P(x):
        """Implementación polinomio P(x)"""
        lag = 0
        for k, p in enumerate(datos):
            lag += p[1]*L(k, x)
            return lag
        
    return P
