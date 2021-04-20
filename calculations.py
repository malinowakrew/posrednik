import copy

from alfabeta import *

class Error(Exception):
    pass


class OverrunLimit(Error):
    def __init__(self, message="Overrun iteration limit") -> None:
        self.message = message
        super().__init__(self.message)


def calculate_transport_matrix(s, d, p):
    if True:
        path = np.zeros((3, 3))

        demand = list(d)
        supply = list(s)
        profit = p[:-1, :-1]

        while True:
            if profit[np.isnan(profit)].size == profit.size:
                break
            else:
                item = np.nanmax(profit)
                item_row, item_col = np.nonzero(profit == item)
                index_of_max = list(map(int, [item_row[0], item_col[0]]))

            path[index_of_max[0], index_of_max[1]] = min(supply[int(index_of_max[0])], demand[int(index_of_max[1])])

            pom_list = supply[:]
            pom = pom_list[int(index_of_max[0])]
            supply[int(index_of_max[0])] = max(0, supply[int(index_of_max[0])] - demand[int(index_of_max[1])])
            demand[int(index_of_max[1])] = max(0, demand[index_of_max[1]] - pom)

            if demand[int(index_of_max[1])] == 0:
                profit[:, index_of_max[1]] = [np.nan, np.nan]
            if supply[int(index_of_max[0])] == 0:
                profit[index_of_max[0], :] = [np.nan, np.nan]

        path[:2, 2] += supply[:2]
        path[2, :2] += demand[:2]
        path[2, 2] = supply[2] - path[2, 1] - path[2, 0]

        print(path)
        return path



def optimal_path_calculation(path, profit):
    if True:
        stop = 20
        while stop:
            print("stop")
            alfa, beta = alfa_beta(path, profit)
            delta_zmienna = delta(path, profit, alfa, beta)

            if np.any(delta_zmienna > 0.0):
                path = cycle(path, delta_zmienna)
            else:
                break
            stop -= 1

        if stop == 0:
            raise OverrunLimit

        return path


def calculate_transport_matrix_grzes(d, s, p):
    profit = copy.deepcopy(p)
    demand = copy.deepcopy(d)
    supply = copy.deepcopy(s)


    zyski = []
    for list_1d in profit:
        for el in list_1d:
            zyski.append(el)
    transport = [[0 for j in range(3)] for i in range(3)]
    for el in range(5):
        list_of_cordinates = np.where(profit == np.amax(zyski))
        zyski.remove(np.amax(zyski))
        x = int(list_of_cordinates[0][0])
        y = int(list_of_cordinates[1][0])
        while transport[x][y] is None:
            list_of_cordinates = np.where(profit == np.amax(zyski))
            zyski.remove(np.amax(zyski))
            x = int(list_of_cordinates[0][0])
            y = int(list_of_cordinates[1][0])
            profit[x][y] = None
        if demand[x] <= supply[y]:
            supply[y] -= demand[x]
            transport[x][y] = demand[x]
            demand[x] -= demand[x]
            for index, element in enumerate(transport[x]):
                if element == 0:
                    transport[x][index] = None
        else:
            demand[x] -= supply[y]
            transport[x][y] = supply[y]
            supply[y] -= supply[y]
            for index, element in enumerate(transport):
                if element[y] == 0:
                    transport[index][y] = None
    for index_x, x in enumerate(transport):
        for index_y, y in enumerate(x):
            if y is None:
                transport[index_x][index_y] = 0
    return transport


def calculate_profit(path, profit):
    # full_profit = 0
    # for index_x, el in enumerate(path):
    #     for index_y, value in enumerate(el):
    #         if value is not None:
    #             full_profit += path[index_x][index_y] * profit[index_x][index_y]
    # print(f"full {full_profit}")
    return np.sum(path*profit)


def check_delta(delta1, transport_matrix, p):
    for el_list in delta1:
        for el in el_list:
            if el > 0:
                alfa, beta = alfa_beta(transport_matrix, p)
                delta1 = delta(transport_matrix, p, alfa, beta)
                cycle(delta1, transport_matrix)
                check_delta(delta1, transport_matrix, p)
    return transport_matrix


def final_calculation(d, s, p, matrix_selling_cost, matrix_cost_buy, matrix_cost_trans):
    profit = p.copy()
    path = calculate_transport_matrix(s, d, p)
    transport_matrix = optimal_path_calculation(path, p)

    whole_profit = calculate_profit(transport_matrix, matrix_selling_cost)
    whole_cost = calculate_profit(transport_matrix, (matrix_cost_trans+matrix_cost_buy))
    ending_profit = calculate_profit(transport_matrix, profit)

    return transport_matrix, ending_profit, whole_profit, whole_cost



