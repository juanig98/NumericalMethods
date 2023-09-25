"""
Hallar el punto de intersección en I [0.5; 2] de las funciones 
por el método de Regula-Falsi con un error < 0.0001.

f(x) = x^3 - x + 1      y 
f(x) = 2x^2

R: x =~ 0.554958
"""

from U3SystemsNoLinear.methods.RegulaFalsi import RegulaFalsi


class ExerciseUsingRegulaFalsi2:
    def statement(self,):
        print("\nEjercicio 4")
        print("-"*80)
        print(
            "\n\nHallar el punto de intersección en I [0.5; 2] de las funciones \npor el método de Regula-Falsi con un error < 0.0001.\n\nf(x) = x^3 - x + 1 y \nf(x) = 2x^2\n\nR: x =~ 0.554958\n")
        print("\nSolución")
        print("-"*80)

    def func(self, x):
        return (x**3 - x + 1) - (2*x**2)  # Se igualan las funciones!

    tol = 0.0001
    a = 0.5
    b = 2

    def resolve(self,):
        self.statement()
        print("Resultado: {}"
              .format(RegulaFalsi(
                  f=self.func,
                  p0=self.a,
                  p1=self.b,
                  tol=self.tol,
                  n=100,
              )
              ))
