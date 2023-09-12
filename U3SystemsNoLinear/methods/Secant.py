def Secant(f, p0, p1, tol, n):
    """
    Implementación método de la secante
    Entradas:
        f -- función
        p0 -- aproximación inicial
        p1 -- aproximación inicial
        tol -- tolerancia
        n -- número máximo de iteraciones
        45Salida:
        p aproximación a cero de f
    None en caso de iteraciones agotadas
    """

    i = 2
    while i <= n:
        p = p1 - (f(p1)*(p1 - p0))/(f(p1) - f(p0))

        print("Iter = {0:<2}, p = {1:.12f}".format(i, p))

        if abs(p - p1) < tol:
            return p
        p0 = p1
        p1 = p
        i += 1

    print("Iteraciones agotadas: Error!")
    return None
