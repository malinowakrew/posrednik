from cycles import *


def alfa_beta(matrix_transport, matrix_profit_arr):
    alpha = [0.0, np.NaN, np.NaN]
    beta = [np.NaN, np.NaN, np.NaN]

    path = matrix_transport.copy()
    profit = matrix_profit_arr.copy()

    for nr_row, row in enumerate(path):
        for nr_col, item in enumerate(row):
            for nr_item in range(nr_row, 3):
                if path[nr_item, nr_col] != 0:
                    if alpha[nr_item] is np.NaN and beta[nr_col] is not np.NaN:
                        alpha[nr_item] = profit[nr_item, nr_col] - beta[nr_col]

                    if beta[nr_col] is np.NaN and alpha[nr_item] is not np.NaN:
                        beta[nr_col] = profit[nr_item, nr_col] - alpha[nr_item]

    return alpha, beta


def delta(matrix_transport, matrix_profit, betatab, alfatab):
    alfa = np.array(alfatab)
    beta = np.array(betatab)

    delta = matrix_profit - np.stack((alfa, alfa, alfa), axis=0) - np.stack((beta, beta, beta), axis=1)

    rows, columns = np.where(matrix_transport != 0.0)

    for x, y in zip(rows, columns):
        delta[x, y] = np.nan

    return delta
