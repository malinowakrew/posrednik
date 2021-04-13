import copy

import numpy as np

d = [10, 28, 50]
s = [20, 30, 38]
p = [[12, 1, 0], [6, 4, 0], [0, 0, 0]]


def calculate(d, s, p):
    profit = copy.deepcopy(p)
    demand = copy.deepcopy(d)
    supply = copy.deepcopy(s)
    zyski = []
    for list_1d in profit:
        for el in list_1d:
            zyski.append(el)
    tmp_list = [[0 for j in range(3)] for i in range(3)]
    for el in range(5):
        list_of_cordinates = np.where(profit == np.amax(zyski))
        zyski.remove(np.amax(zyski))
        x = int(list_of_cordinates[0][0])
        y = int(list_of_cordinates[1][0])
        while tmp_list[x][y] is None:
            list_of_cordinates = np.where(profit == np.amax(zyski))
            zyski.remove(np.amax(zyski))
            x = int(list_of_cordinates[0][0])
            y = int(list_of_cordinates[1][0])
            profit[x][y] = None
        if demand[x] <= supply[y]:
            supply[y] -= demand[x]
            tmp_list[x][y] = demand[x]
            demand[x] -= demand[x]
            for index, element in enumerate(tmp_list[x]):
                if element == 0:
                    tmp_list[x][index] = None
        else:
            demand[x] -= supply[y]
            tmp_list[x][y] = supply[y]
            supply[y] -= supply[y]
            for index, element in enumerate(tmp_list):
                if element[y] == 0:
                    tmp_list[index][y] = None
    for index_x, x in enumerate(tmp_list):
        for index_y, y in enumerate(x):
            if y is None:
                tmp_list[index_x][index_y] = 0
    return tmp_list


def calculate_profit(path, profit):
    full_profit = 0
    for index_x, el in enumerate(path):
        for index_y, value in enumerate(el):
            if value is not None:
                full_profit += path[index_x][index_y] * profit[index_x][index_y]
    return full_profit


xd = calculate(d, s, p)
ksd = calculate_profit(xd, p)
for el in xd:
    print(el)
print(ksd)
