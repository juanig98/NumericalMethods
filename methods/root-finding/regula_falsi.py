from math import *

def pol(x):
    """Función de prueba"""
    return x**3 + 4*x**2 - 10 # retorna pol(x) = x^3 + 4x^2 − 10

def trig(x):
    """Función de prueba"""
    return x*cos(x-1) - sin(x) # retorna trig(x) = x cos(x − 1) − sin(x)

def pote(x):
    """Función de prueba"""
    return pow(7, x) - 13 # retorna pote(x) = 7x − 13

def regula(f, p0, p1, tol, n):
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
        print("Iter = {0:<2}, p = {1:.12f}".format(i, p))
        if abs(p - p1) < tol:
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

"""
TESTING:
# pol(x), a = 1.0, b = 2.0, T OL = 10−8, N0 = 100
print("Regula falsi función pol(x):")
regula(pol, 1, 2, 1e-8, 100)

# trig(x), a = 4.0, b = 6.0, T OL = 10−8, N0 = 100
print("Regula falsi función trig(x):")
regula(trig, 4, 6, 1e-8, 100)

# pote(x), a = 0, b = 2.0, T OL = 10−8, N0 = 100
print("Regula falsi función pote(x):")
regula(pote, 0, 2, 1e-8, 100)
"""