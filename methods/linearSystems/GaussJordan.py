import numpy as np


def GaussJordan(A, B):
    # A: Matriz de coeficientes
    # B: Vector de términos independientes

    n = len(A)
    m = n + 1
    AugmentedMatrix = np.hstack((A, B.reshape(-1, 1)))

    for i in range(n):
        pivot_idx = i
        for j in range(i + 1, n):
            if abs(AugmentedMatrix[j, i]) > abs(AugmentedMatrix[pivot_idx, i]):
                pivot_idx = j

        AugmentedMatrix[[i, pivot_idx], :] = AugmentedMatrix[[pivot_idx, i], :]

        pivot = AugmentedMatrix[i, i]
        AugmentedMatrix[i, :] /= pivot

        for j in range(n):
            if j != i:
                factor = AugmentedMatrix[j, i]
                AugmentedMatrix[j, :] = AugmentedMatrix[j, :] - \
                    factor * AugmentedMatrix[i, :]

    solutions = AugmentedMatrix[:, n]

    return solutions
