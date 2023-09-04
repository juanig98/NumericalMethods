import numpy as np
"""MÉTODO DE GAUSS JORDAN
        Este método difiere con el método de eliminación gaussiana puesto que cuando se elimina 
        una incógnica no sólo se elimina de las ecuaciones siguientes sino de todas las otras
        ecuaciones. De esta forma el paso de eliminación genera una matriz identidad en lugar 
        de una matriz triangular. Por consiguiente no es ncesario emplear la sustitución hacía 
        atrás para obtener la solución.
"""

def GaussJordan(A, B, proc=False):
    # A: Matriz de coeficientes
    # B: Vector de términos independientes

    n = len(A)
    m = n + 1
    Amp = np.hstack((A, B.reshape(-1, 1)))

    if proc:
        print("\nMatriz inicial:\n\n{}\n\n".format(Amp))

    for i in range(n):
        pivot = i

        if proc:
            print("---------------------------------------- Paso {} ----------------------------------------".format(i+1))
        for j in range(i + 1, n):
            if abs(Amp[j, i]) > abs(Amp[pivot, i]):
                pivot = j

        if pivot != i and proc:
            print("- Se reemplaza F{} por F{}".format(i+1, pivot+1))

        Amp[[i, pivot], :] = Amp[[pivot, i], :]

        pivot = Amp[i, i]
        Amp[i, :] /= pivot

        if proc:
            print("- Se divide la F{} por {} (pivot)\n\nMatriz:\n{}\n"
                  .format(i, pivot, Amp))

        for j in range(n):
            if j != i:
                factor = Amp[j, i]
                Amp[j, :] = Amp[j, :] - \
                    factor * Amp[i, :]

                if proc:
                    print("- Se resta la F{} por la F{} multiplicado por {}"
                          .format(j+1, i+1, factor))

        if proc:
            print("\nMatriz resultante del paso {}:\n{}\n"
                  .format(i, Amp))

    return Amp[:, n]
