import math
from U3SystemsNoLinear.methods.Bisection import Bisection

from U3SystemsNoLinear.methods.Newton import Newton
from U3SystemsNoLinear.methods.Secant import Secant
"""
Resuelva las ecuaciones siguientes con f(x) < 0.001:
i)   f(x) =  e^x- 5x^2 = 0      aproximación: -5        R: -0.371427
ii)  f(x) =  x^3- 2x -1 = 0     xn = 2.4; xn-1 = 2.5    R: 1.6180624
iii) f(x) = √x + 2 - x = 0      I[3.5; 5.5]             R: 4.000008002





"""


class Exercise7:
    def statement(self,):
        print("\nEjercicio 7")
        print("-"*80)
        print(
            "\n\nResuelva las ecuaciones siguientes con f(x) < 0.001:\ni)   f(x) =  e^x- 5x^2 = 0\taproximación: -5\t  R: -0.371427\nii)  f(x) =  x^3- 2x -1 = 0\txn = 2.4; xn-1 = 2.5\tR: 1.6180624\niii) f(x) = √x + 2 - x = 0\tI[3.5; 5.5]\tR: 4.000008002\n")
        print("\nSolución")
        print("-"*80)
    TOL = 0.001

    class Item1:
        """
        f(x) =  e^x- 5x^2 = 0      aproximación: -5        R: -0.371427
        """
        p0 = -5
        max_iter = 50

        def f(self, x):
            return math.e ** x - 5*(x**2)

        def fprima(self, x):
            return math.e ** x - 5*x

        def resolve(self,):
            print("Resultado (i): {}"
                  .format(
                      Newton(
                          f=self.f,
                          fprima=self.fprima,
                          p0=self.p0,
                          n=self.max_iter,
                          tol=Exercise7.TOL
                      )
                  )
                  )

    class Item2:
        """
        f(x) =  x^3- 2x -1 = 0     xn = 2.4; xn-1 = 2.5    R: 1.6180624
        """
        xn = 2.4
        xn_1 = 2.5
        max_iter = 50

        def f(self, x):
            return (x**3) - (2*x) - 1

        def resolve(self,):
            print("Resultado (ii): {}"
                  .format(
                      Secant(
                          f=self.f,
                          n=self.max_iter,
                          p0=self.xn,
                          p1=self.xn_1,
                          tol=Exercise7.TOL
                      )
                  ))

    class Item3:
        """
        f(x) = √x + 2 - x = 0      I[3.5; 5.5]             R: 4.000008002
        """
        a = 3.5
        b = 5.5
        max_iter = 20
        # √x + 2 - x = 0

        def f(self, x):
            return math.sqrt(x) + 2 - x

        def resolve(self,):
            print("Resultado (iii): {}"
                  .format(
                      Bisection(
                          a=self.a,
                          b=self.b,
                          f=self.f,
                          n=self.max_iter,
                          tol=Exercise7.TOL
                      )
                  )
                  )
