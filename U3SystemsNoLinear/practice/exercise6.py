import math

from U3SystemsNoLinear.methods.RegulaFalsi import RegulaFalsi
"""
Determinar intervalos de tamaño 1.0, tales que cada uno contenga 
una o más raíces (nº impar de raíces) de 
        Y = -19(x - 0.5)(x - 1) + e^x + e^(-2x)
en el intervalo [-10, 10].

R: [-3, -2] [0, 1]; [1, 2]; [6, 7]
"""


class Exercise6:
    def statement(self,):
        print("\nEjercicio 6")
        print("-"*80)
        print(
            "\n\nDeterminar intervalos de tamaño 1.0, tales que cada uno contenga\nuna o más raíces (nº impar de raíces) de \nY = -19(x - 0.5)(x - 1) + e^x + e^(-2x)\nen el intervalo [-10, 10].\nR: [-3, -2] [0, 1]; [1, 2]; [6, 7]\n")
        print("\nSolución")
        print("-"*80)

    def func(self, x):
        return -19 * (x - 0.5) * (x - 1) + math.e**x + math.e**(-2 * x)

    tol = 0.001

    def resolve(self,):
        self.statement()

        for i in range(20):
            p0 = -10+i
            p1 = -9+i
            print("\n\nPrueba en el intervalo [{},{}]".format(p0,p1))
            print("-"*50)
            print("Resultado : {}"
                  .format(RegulaFalsi(
                      f=self.func,
                      p0=p0,
                      p1=p1,
                      tol=self.tol,
                      n=10,
                  )
                  ))
