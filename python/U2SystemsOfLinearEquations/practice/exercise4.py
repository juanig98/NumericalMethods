import numpy as np

from U2SystemsOfLinearEquations.methods.ElimGauss import ElimGauss

"""
Una empresa se dedica a la fabricación de cuatro tipos de jabón. 
Desde la compra de materias primas hasta la disposición para la
distribución se realizan las siguientes fases:
I) se mezclan los dos tipos de materias pritras utilizadas, grasa
    vegetal y sosa cáustica;
II) se introduce la mezcla obtenida en unos moldes preparados al 
    efecto;
III) los bloques obtenidos en la fase anterior se cortan y 
    troquelan, y
IV) las pastillas así obtenidas se envasan en cajas de cartón de 
    200 unidades.

Los recursos necesarios para producir los cuatro tipos de jabones, 
por caja fabricada, vienen dados pol la siguiente tabla:
------------------------------------------------------------------------
|         S. Mezclado          |   S. Moldeado     |   S. Troquelado   |
------------------------------------------------------------------------
| Jabón | Kg. grasa | Kg. sosa |   Hora/Máquina    |    Hora/Máquina   |
------------------------------------------------------------------------
|  J1   |    20     |   10     |       10          |          3        |
|  J2   |    25     |   15     |       8           |          4        |
|  J3   |    40     |   20     |       10          |          7        |
|  J4   |    50     |   22     |       15          |         20        |
------------------------------------------------------------------------
Si se dispone durante una semana de:
- 1970 Kg de grasa vegetal, 
- 970 Kg de sosa cáustica, 
- 601 hora/máquina en la sección de moldeadaos y 
- 504 horas/máquina en la sección de troquelado. 
¿Cuántas cajas de jabones de cada tipo se pueden producir, utilizando 
todos los recursos disponibles, en una semana?
"""


class ExerciseSoapFactory:
    A = np.array([
        [20.0,  25.0,   40.0,   50.0],
        [10.0,  15.0,   20.0,   22.0],
        [10.0,  8.0,    10.0,   15.0],
        [3.0,   4.0,    7.0,    20.0],
    ])

    b = np.array([
        1970.0,
        970.0,
        601.0,
        504.0
    ])

    def resolve(self,):
        print("Solución:", ElimGauss(self.A, self.b, proc=True))
