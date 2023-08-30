from math import *

def pol(x):
    """Función de prueba"""
    return x**3 + 4*x**2 - 10 # retorna pol(x) = x^3 + 4x^2 − 10

def trig(x):
    """Función de prueba"""
    return x*cos(x-1) - sin(x) # retorna trig(x) = x cos(x − 1) − sin(x)

def bisection(f, a, b, tol, n):
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
        p = a + (b - a)/2
        print("i = {0:<2}, p = {1:.12f}".format(i, p))
       
        if abs(f(p)) <= 1e-15 or (b - a)/2 < tol:
            return p
       
        i += 1
       
        if f(a)*f(p) > 0:
            a = p
        else:
            b = p

    print("Iteraciones agotadas: Error!")
    
    return None

"""
TESTING:

# pol(x), a = 1, b = 2, T OL = 10−8, N0 = 100
print("Bisección función pol(x):")
bisec(pol, 1, 2, 1e-8, 100)

# trig(x), a = 4, b = 6, T OL = 10−8, N0 = 100
print("Bisección función trig(x):")
"""