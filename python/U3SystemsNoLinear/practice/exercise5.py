import math

from U3SystemsNoLinear.methods.Bisection import Bisection
"""
Se sabe que la raíz de e^x - 2 = 0 está en [0, 2].
Hallar un valor aproximado de la raíz con una
tolerancia de e = 0.01.

R: 0.685495
"""


class Exercise5:
    def statement(self,):
        print("\nEjercicio 5")
        print("-"*80)
        print(
            "\n\nSe sabe que la raíz de e^x - 2 = 0 está en [0, 2]. \nHallar un valor aproximado de la raíz con una \ntolerancia de e = 0.01.\n\nR: 0.685495\n")
        print("\nSolución")
        print("-"*80)
        
    def func(self, x):
        return math.e**x - 2

    tol = 0.01
    a = 0
    b = 2

    def resolve(self,):
        self.statement()
        
        print("Resultado: {}"
              .format(Bisection(
                  self.func,
                  self.a,
                  self.b,
                  self.tol,
                  100,
              )))
