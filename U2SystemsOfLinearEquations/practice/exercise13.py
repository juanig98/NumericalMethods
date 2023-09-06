
import numpy as np

from U2SystemsOfLinearEquations.methods.ElimGauss import ElimGauss
"""
Una empresa necesita para la construcción de un proyecto:
    -> Material A   4800 unidades
    -> Material B   5810 unidades
    -> Material C   5690 unidades

Existen en la actualidad 3 canteras donde se obtienen los materiales. 
La siguiente tabla presenta la distribución porcentual de cada material
en cada cantera.

    A => Prod. total de la cantera 1
    B => Prod. total de la cantera 2
    C => Prod. total de la cantera 3
     --------------------------
    |    1   |    2   |    3   |
    |--------------------------|
    |  0,52  |  0,20  |  0,25  |
    |  0,30  |  0,50  |  0,20  |
    |  0,18  |  0,30  |  0,55  |
     --------------------------
¿Cuantas unidades de material se deben extraer en cada cantera para
cumplir con las necesidades de su empresa
Rta: 
    - x1 = 4011.63
    - x2 = 7162.79
    - x3 = 5125.58
"""


class ConstructionCompany:
    A = np.array([
        [0.52,  0.20,   0.25],
        [0.30,  0.50,   0.20],
        [0.18,  0.30,   0.55],
    ], float)

    B = np.array([
        4800.0,
        5810.0,
        5690.0,
    ], float)

    def resolve(self,):
        print("Solución:",
              ElimGauss(self.A,
                        self.B, True))
