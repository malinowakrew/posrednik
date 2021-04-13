from cycles import *


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
        pom = pom + 1

    return alfa, beta


def delta(matrix_transport, matrix_profit, betatab, alfatab):
    alfa = np.array(alfatab)
    beta = np.array(betatab)

    delta = matrix_profit - np.stack((alfa, alfa, alfa), axis=0) - np.stack((beta, beta, beta), axis=1)

    rows, columns = np.where(matrix_transport != 0.0)

    for x, y in zip(rows, columns):
        delta[x, y] = np.nan

    return delta
