import math

from U3SystemsNoLinear.methods.Bisection import Bisection
"""
Aplicar el método de la bisección para hallar la raíz de la
ecuación f(x) = x2 - sen(x) = 0, en el intervalo [0.1; 1.57] 
con un error < 0.001

R: 0.8766309
"""

class ExerciseUsingBisection2:
    def func(self, x):
        return x**2 - math.sin(x)
    TOL = 0.001
    a = 0.1
    b = 1.57

    def resolve(self,):
        print("Solución: {}"
              .format(Bisection(
                  f=self.func,
                  a=self.a,
                  b=self.b,
                  tol=self.TOL,
                  n=100,
              )
              ))
