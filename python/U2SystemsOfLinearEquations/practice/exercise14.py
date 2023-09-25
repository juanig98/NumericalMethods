import numpy as np

from U2SystemsOfLinearEquations.methods.ElimGauss import ElimGauss
"""
Supongamos que en un sistema biológico existen 3 especies de animales y
3 fuentes de alimentos. Tomemos a bi (i-esimo alinento) para representar
la cantidad diaria disponible de alimento y aij la cantidad del i-esimo
alimento consumido por la j-esima especie en carácter promedio.

El sistema viene dado de la siguiente forma:
          |  2   0   3  |
A = aij = |  0   2   2  |
          |  0   1   3  |

         |  3500  |
B = bi = |  2000  | cantidad de alimento 
         |  1300  |

representa el equilibrio donde hay un suministro diario de alimento 
necesario en promedio para cada especie

Preguntas:
    - ¿Cuál es el número exacto de cada especie que satisface el sistema propuesto?
    - Dado este conjunto solución ¿Es suficielte la cantidad de alimento para 
        satisfacer el consumo promedio diario?

"""


class BiologicalSystem:
    A = np.array([
        [2.0,  0.0,   3.0],
        [0.0,  2.0,   2.0],
        [0.0,  1.0,   3.0],
    ], float)

    B = np.array([
        3500.0,
        2000.0,
        1300.0,
    ], float)

    def resolve(self,):
        print("Solución:",
              ElimGauss(self.A,
                        self.B, True))
