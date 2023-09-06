from U3SystemsNoLinear.methods.Bisection import Bisection

"""
Aplicar el método de la bisección a f(x) = x3 - 17 = 0, 
a fin de determinar la raíz cúbica de 17 con un error
menor que 0.125. Iniciar los cálculos en el intervalo [2; 3].

R: 2.5703125
"""


class ExerciseUsingBisection1:
    def func(self, x):
        return x**3 - 17
    TOL = 0.125
    a = 2
    b = 3

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
