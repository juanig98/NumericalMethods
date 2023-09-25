import math

from U3SystemsNoLinear.methods.RegulaFalsi import RegulaFalsi
"""
Aplicar el método de Regula-Falsi para hallar la raíz de la 
ecuación f(x) = sen(x) - e^(-x) = 0, en el intervalo [0.5; 1]
con un error < 0.00001

R: 0.5885327
"""


class ExerciseUsingRegulaFalsi1:
    def statement(self,):
        print("\n\n")
        print("-"*80)
        print(
            "\nEjercicio 3\n\nAplicar el método de Regula-Falsi para hallar la raíz de la\necuación f(x) = sen(x) - e^(-x) = 0, en el intervalo [0.5; 1]\ncon un error < 0.00001\n\nR: 0.5885327\n"
        )

    def func(self, x):
        return math.sin(x) - math.e**(-x)
    TOL = 0.00001
    a = 0.5
    b = 1

    def resolve(self,):
        self.statement()
        print("Solución: {}"
              .format(RegulaFalsi(
                  f=self.func,
                  p0=self.a,
                  p1=self.b,
                  tol=self.TOL,
                  n=100,
              )
              ))
