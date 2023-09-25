"""
El número, en miles de habitantes, de una determinada ciudad 
ha evolucionado según los datos de la siguiente tabla: 

Años        1987    1988    1990
Poblacion    53      71      91

Ajustar por Lagrange un polinomio cuadrático a los datos y
estimar la población que tenía esa ciudad en el año 1989

Rta: 83,667
"""


from U4InterpolationAndAproximation.methods.Lagrange import LagrangePol


class ExercisePeopleCity1989:
    def resolve(self,):
        # self.statement()
        Pf = LagrangePol([
            (1987, 53),
            (1988, 71),
            (1990, 91)
        ])
        import numpy as np
        from scipy.interpolate import lagrange
        x = np.array([0, 1, 2])
        y = x**3
        poly = lagrange(x, y)
        
        print("Resultado: {}"
              .format(Pf(1989)))
