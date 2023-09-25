from math import *


def RegulaFalsi(f, p0, p1, tol, n):
    """
    Implementación método de regula falsi
    Entradas:
    f -- función
    p0 -- aproximación inicial
    p1 -- aproximación inicial
    tol -- tolerancia
    n -- número máximo de iteraciones
    Salida:
    p aproximación a cero de f
    None en caso de iteraciones agotadas
    """
    i = 0
    while i <= n:
        q0 = f(p0)
        q1 = f(p1)
        p = p1-(q1*(p1 - p0))/(q1 - q0)
        err = abs(p - p1)
        print("Iteracion {0:<1}: \tp = {1:.12f}\tError: {2:.12f}".format(i, p, err))
        if abs(p - p1) < tol:
            print("\nSe superó la tolerancia máxima!\nEl error es de {} menor a la tolerancia de {}\n"
                  .format(err, tol))
            return p
        i += 1
        q = f(p)
        if q*q1 < 0:
            p0 = p1
            q0 = q1
        p1 = p
        q1 = q

    print("Iteraciones agotadas: Error!")
    return None
