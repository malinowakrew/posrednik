import numpy as np
from math import isnan


def alfa_beta(matrix_transport, matrix_profit):
    alfa = [0, np.nan, np.nan]
    beta = [np.nan, np.nan, np.nan]

    rows, columns = np.where(matrix_transport != 0.0)

    pom = 0
    while np.any(np.isnan(beta)) or np.any(np.isnan(alfa)) and pom < 100:
        for x, y in zip(rows, columns):
            if isnan(alfa[x]) and not (isnan(beta[y])):
                alfa[x] = matrix_profit[x, y] - beta[y]
            elif not (isnan(alfa[x])) and isnan(beta[y]):
                beta[y] = matrix_profit[x, y] - alfa[x]
        pom = pom+1

    return alfa, beta


if __name__ == "__main__":
    matrix_transport = np.array([[10.,  0.,  0.],[10., 18.,  0.],[ 0., 12., 38.]])
    matrix_profit = np.array([[12.0, 1.0, 0.0],[6.0, 4.0, 0.0], [0.0, 0.0, 0.0]])
    print(alfa_beta(matrix_transport, matrix_profit))