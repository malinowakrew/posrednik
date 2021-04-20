from cycles import *


# def alfa_beta(matrix_transport, matrix_profit):
#     alfa = [0, np.nan, np.nan]
#     beta = [np.nan, np.nan, np.nan]
#
#     rows, columns = np.where(matrix_transport != 0.0)
#
#     pom = 0
#     while np.any(np.isnan(beta)) or np.any(np.isnan(alfa)) and pom < 100:
#         for x, y in zip(rows, columns):
#             if isnan(alfa[x]) and not (isnan(beta[y])):
#                 alfa[x] = matrix_profit[x, y] - beta[y]
#             elif not (isnan(alfa[x])) and isnan(beta[y]):
#                 beta[y] = matrix_profit[x, y] - alfa[x]
#         pom = pom + 1
#
#     return alfa, beta



def alfa_beta(path, profit):
    alpha = [0.0, np.NaN, np.NaN]
    beta = [np.NaN, np.NaN, np.NaN]

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
