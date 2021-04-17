import copy

import numpy as np

from alfabeta import *


def calculate_transport_matrix(d, s, p):
    profit = copy.deepcopy(p)
    demand = copy.deepcopy(d)
    supply = copy.deepcopy(s)

    print(profit)
    print(demand)
    print(supply)

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
    full_profit = 0
    for index_x, el in enumerate(path):
        for index_y, value in enumerate(el):
            if value is not None:
                full_profit += path[index_x][index_y] * profit[index_x][index_y]
    return full_profit


def check_delta(delta1, transport_matrix, p):
    for el_list in delta1:
        for el in el_list:
            if el > 0:
                alfa, beta = alfa_beta(transport_matrix, p)
                delta1 = delta(transport_matrix, p, alfa, beta)
                cycle(delta1, transport_matrix)
                check_delta(delta1, transport_matrix)
    return transport_matrix


def final_calculation(d, s, p):
    transport_matrix = calculate_transport_matrix(d, s, p)
    transport_matrix = np.array(transport_matrix)
    p = np.array(p)
    alfa, beta = alfa_beta(transport_matrix, p)
    delt = delta(transport_matrix, p, alfa, beta)
    transport_matrix = check_delta(delt, transport_matrix, p)
    whole_profit = calculate_profit(transport_matrix, p)
    return transport_matrix, whole_profit
