import numpy as np

from U2SystemsOfLinearEquations.methods.ElimGauss import ElimGauss
"""
Una compañia minera trabaja en 3 minas, cada una de ellas produce 3 clases 
de minerales:
- La 1° mina puede producir:
    -> Mineral A    4 t/h
    -> Mineral B    3 t/h
    -> Mineral C    5 t/h
- La 2° mina puede producir:
    -> Mineral A    1 t/h
    -> Mineral B    1 t/h
    -> Mineral C    1 t/h
- La 3° mina puede producir:
    -> Mineral A    2 t/h
    -> Mineral B    4 t/h
    -> Mineral C    3 t/h

¿Cuantas horas se debe trabajar en cada mina para satisfacer el siguiente
pedido?
    A = 19 toneladas
    B = 25 toneladas
    C = 25 toneladas
"""


class MiningCompany:
    A = np.array([
        [4.0, 1.0, 2.0],
        [3.0, 1.0, 4.0],
        [5.0, 1.0, 3.0],
    ], float)

    B = np.array([
        19.0,
        25.0,
        25.0,
    ], float)

    def resolve(self,):
        print("Solución:",
              ElimGauss(self.A,
                        self.B, True))
