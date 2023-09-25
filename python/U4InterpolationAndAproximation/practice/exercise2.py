"""
Dada la siguiente tabla:
Xk      -1  0  3  7
f(xk)    2  0  4  7
"""

from U4InterpolationAndAproximation.methods.Lagrange import LagrangePol


class Exercise:
    p0 = (0, -2)
    p1 = (1, 6)
    p2 = (3, 40)

    def resolve(self,):
        # self.statement()
        Pf = LagrangePol([
            (0, -2),
            (1, 6),
            (3, 40)
        ])
        
        print("Resultado: {}"
              .format(Pf(2)))
