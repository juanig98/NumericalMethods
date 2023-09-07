import math
from U3SystemsNoLinear.methods.Bisection import Bisection
"""
Aplicar el método de la bisección para hallar la raíz de la
ecuación f(x) = x2 - sen(x) = 0, en el intervalo [0.1; 1.57]
con un error < 0.001

R: 0.8766309
"""


class ExerciseUsingBisection2:
    def statement(self,):
        print("\n")
        print("-"*80)
        print(
            "\nEjercicio 2\n\nAplicar el método de la bisección para hallar la raíz de la\necuación f(x) = x2 - sen(x) = 0, en el intervalo [0.1; 1.57]\ncon un error < 0.001\nR: 0.8766309\n")

    def func(self, x):
        return x**2 - math.sin(x)
    TOL = 0.001
    a = 0.1
    b = 1.57

    def resolve(self,):
        self.statement()
        print("Solución: {}"
              .format(Bisection(
                  f=self.func,
                  a=self.a,
                  b=self.b,
                  tol=self.TOL,
                  n=100,
              )
              ))
