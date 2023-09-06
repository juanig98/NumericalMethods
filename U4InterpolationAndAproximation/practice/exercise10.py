"""
- Desarrole una función denominada FLAGR que evalúe para el argumento 
de interpolación x, el polinomio de interpolación Lagrange de grado d
que pase por el conjunto de puntos 
    (xmin,ymin), (xmin+1,ymin+1)........, (xmin+d,ymin+d), 

donde min indica la posición del punto en la tabla.
A continuación escriba un programa principal que lea datos 
    x1,x2,....xn ,y1,y2,....yn, x, d,min; 
llame a FLAGR para el cálculo del polinomo de interpolación apropiado 
y escuentre el valor de la interpolación y(x). 

Como datos de comprobación utilice la tabla 1 que relaciona los datos
observados de voltaje y temperatura (en grados Farenheit °F) para
termopares formados por Platino y Platino- diez por ciento Rodio con 
juntas refrigeradas a 32°

| Tabla 1 | emf (microvoltios) | Temperatura (°F) |
|    1    |      0             |         32.0     |
|    2    |      500           |        176.0     |
|    3    |      1000          |        296.4     |
|    4    |      1500          |        405.7     |
|    5    |      2000          |        509.0     |
|    6    |      2500          |        608.4     |
|    7    |      3000          |        704.7     |
|    8    |      3500          |        799.0     |
|    9    |      4000          |        891.9     |
|    1    |      4500          |        983.0     |
|    1    |      5000          |       1072.6     |
|    1    |      5500          |       1160.8     |
|    1    |      6000          |       1247.5     |

| emf (microvoltios) | Temperatura (°F) | min | d |
|        300         |       122.4      |   1 | 2 |
|       1700         |       447.6      |   3 | 3 |
|       3300         |       761.4      |   5 | 5 |
|       5300         |      1125.7      |  10 | 3 |
|       5900         |      1230.3      |  11 | 2 |

Léanse de la Tabla1, los valores tabulados para los 13 puntos base 
seleccionados x1=0, x2=500, x3=1000, ..... x13=6000 y los correspondiente 
valores funcionales y1 ,y2 ,y3....... y13 en donde yi = f(xi). 
Llámese posteriormente a FLAGR para calcular y(x) para argumentos 
x=300, 1700, 3300, 5300 y 5900, con los respectivos valores de d y min.
que figuran en la tabla 2. Compárense los resultados con los de dicha tabla
(columna temperatura). 
"""

class Exercise:
    def resolve():
        pass