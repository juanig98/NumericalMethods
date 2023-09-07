from math import *


def Bisection(f, a, b, tol, n):
    """
    Implementación método de bisección
    Entradas:
    f -- función
    a -- inicio intervalo
    b -- fin intervalo
    tol -- tolerancia
    n -- número máximo de iteraciones
    Salida:
    p aproximación a cero de f
    None en caso de iteraciones agotadas
    """
    i = 1
    while i <= n:
        err = (b - a)/2
        p = a + err
        print(
            "Iteración {0:<1}: \t\tp = {1:.12f}\t\tError: {2:.12f}".format(i, p, err))

        if abs(f(p)) <= 1e-15 or err <= tol:
            print("\nSe superó la tolerancia máxima!\nEl error es de {} menor a la tolerancia de {}\n"
                  .format(err, tol))
            return p

        i += 1

        if f(a)*f(p) > 0:
            a = p
        else:
            b = p

    print("Iteraciones agotadas: Error!")

    return None
