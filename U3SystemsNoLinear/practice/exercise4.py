"""
Hallar el punto de intersección en I [0.5; 2] de las funciones 
por el método de Regula-Falsi con un error < 0.0001.

f(x) = x^3 - x + 1      y 
f(x) = 2x^2

R: x =~ 0.554958
"""

from U3SystemsNoLinear.methods.RegulaFalsi import RegulaFalsi


class ExerciseUsingRegulaFalsi2:
    def func1(self, x):
        return x**3 - x + 1
    def func2(self, x):
        return x**2 
    TOL = 0.0001
    a = 0.5
    b = 2

    def resolve(self,):
        print("Solución: {}"
              .format(RegulaFalsi(
                  f=self.func1,
                  p0=self.a,
                  p1=self.b,
                  tol=self.TOL,
                  n=100,
              )
              ))
