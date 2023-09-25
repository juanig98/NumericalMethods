"""
Ajuste polinomios de orden 1,2 y 3 a los siguientes datos 
y determine cual de ellos aproxima mejor.
|    x  |    y   |
|    0  |    0   |
| 0.002 |  0.618 |
| 0.004 | 1.1756 |
| 0.006 |  1.618 |
| 0.008 | 1.9021 |

Nota para determinar el error que se comete al aproximar un
polinomio a una nube de n puntos, utilizar la sigueinte expresión:
        E = Σ(p(xk) - f_k)^2

Rta: 
- y = 240.21x + 0.1019
- y = -13982x^2 + 352.07x - 0.01

Mejor ajuste: y= -1E+06x^3 - 1744x^2 + 316.99x - 0.0002
"""

class Exercise:
    def resolve():
        pass