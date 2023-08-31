import numpy as np


def ElimGauss(A, B):
    # A: Matriz de coeficientes
    # B: Vector de terminos independientes
    # Amp: Matriz ampliada
    # X: Vector de resultados

    bb = len(B)
    n = len(A)

    if n != bb:
        print('Error: puede que la matriz de coeficientes no sea cuadrada, o falten datos al vector de terminos independientes')

    elif np.linalg.det(A) == 0:
        print('Error: La matriz es singular, su determinante es igual a cero')

    else:
        m = n + 1
        Amp = np.hstack((A, B.reshape(-1, 1)))
        p = 0

        for i in range(1, n):
            k = i - 1

            # Ordenamiento y pivoteo
            max_idx = np.argmax(np.abs(Amp[k:n, k]))
            b = max_idx + p
            Amp[[k, b], :] = Amp[[b, k], :] 

            # Etapa hacia adelante (Eliminacion)
            for j in range(i, n):
                r = float(Amp[j, k]) / float(Amp[k, k])
                Amp[j, :] = Amp[j, :] - (r * Amp[k, :])

            p += 1

        # Muestra la matriz después de la eliminación
        print('Matriz triangular (después de la eliminación)')
        print(Amp)

        # Etapa hacia atrás (cálculo de incógnitas)
        X = np.zeros(n)
        for i in range(n - 1, -1, -1):

            X[i] = (Amp[i, m-1] - np.sum(Amp[i, i+1:n] * X[i+1:n])) / Amp[i, i]

        print('Vector de resultados')

        return X
