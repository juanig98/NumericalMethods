import numpy as np
"""MÉTODO DE ELIMINACIÓN DE GAUSS
        Sea el S.E.L. (Sistema de Ecuaciones Lineales) A.X = C, el método de consiste en transformar 
    la matriz A y concurrentemente el vector C hasta obenter un S.E.L. equivalente (con la misma
    solución) que sea triangular superior. 
    
        El procedimiento consta de dos pasos:
            1. Eliminación hacia adelante de incógnitas.
            2. Sustitución hacia atrás.
"""

def ElimGauss(A, B, proc=False):
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

        if proc:
            print("\nMatriz inicial:\n\n{}".format(Amp))

        for i in range(1, n):
            k = i - 1

            if proc:
                print("\nPaso {}: ".format(i))

            # Ordenamiento y pivoteo
            max_idx = np.argmax(np.abs(Amp[k:n, k]))
            b = max_idx + p
            Amp[[k, b], :] = Amp[[b, k], :]

            # Marco el pivot
            if proc:
                print("\n - F{} se divide por {} (marcado de pivot)"
                      .format(k+1, Amp[k, k]))
            Amp[k, :] = Amp[k, :] / Amp[k, k]

            # Etapa hacia adelante (Eliminacion)
            for j in range(i, n):
                r = float(Amp[j, k]) / float(Amp[k, k])
                Amp[j, :] = Amp[j, :] - (r * Amp[k, :])
                if proc:
                    print("\n - F{} se resta por la F{} multiplicado por {}"
                          .format(j+1, k+1, r))
                    print("\n" + str(Amp))

            p += 1

            if i == n-1:
                if proc:
                    print("\n - F{} se divide por {}"
                          .format(i, Amp[i, i]))
                    Amp[i, :] = Amp[i, :] / Amp[i, i]

        # Muestra la matriz después de la eliminación
        if proc:
            print('\n\nMatriz triangular (después de la eliminación)\n\n {}\n'
                  .format(str(Amp)))

        # Etapa hacia atrás (cálculo de incógnitas)
        X = np.zeros(n)
        for i in range(n - 1, -1, -1):
            X[i] = (Amp[i, m-1] - np.sum(Amp[i, i+1:n] * X[i+1:n])) / Amp[i, i]

        return X
