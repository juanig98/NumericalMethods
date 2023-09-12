def Newton(f, fprima, p0, tol, n):
    """
    Implementación método de Newton
    Entradas:
    f -- función
    fprima -- derivada función f
    p0 -- aproximación inicial
    tol -- tolerancia
    n -- número máximo de iteraciones

    Salida:
    p aproximación a cero de f
    None en caso de iteraciones agotadas
    """
    i = 1
    while i <= n:
        p = p0 - f(p0)/fprima(p0)
        print("Iter = {0:<2}, p = {1:.12f}".format(i, p))
        if abs(p - p0) < tol:
            return p
        p0 = p
        i += 1
    print("Iteraciones agotadas: Error!")
    return None
