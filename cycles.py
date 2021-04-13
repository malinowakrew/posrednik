from math import isnan

import numpy as np


def cycle(delta, matrix_transport):
    rows, columns = np.where(delta > 0.0)

    #print(rows, columns)
    for x, y in zip(rows, columns):
        for x_nr, x_item in enumerate(delta[x, :]):
            if isnan(x_item):
                #print(f" x {x_item} on iter {x_nr}")
                for y_nr, y_item in enumerate(delta[:, y]):
                    if isnan(y_item):
                        #print(f"{y_item} on iter {y_nr}")
                        #print(f"testowanie przecięcia {delta[y_nr, x_nr]} na {y_nr} {x_nr}")
                        if isnan(delta[y_nr, x_nr]):
                            #print(("Przed"))
                            #print(matrix_transport)
                            minvalue = min(matrix_transport[y_nr, x_nr], matrix_transport[y_nr, y],
                                           matrix_transport[x, x_nr])
                            #print(f"min {minvalue}")
                            matrix_transport[x, y] += minvalue
                            matrix_transport[y_nr, x_nr] += minvalue
                            matrix_transport[y_nr, y] -= minvalue
                            matrix_transport[x, x_nr] -= minvalue

                            return matrix_transport

    return matrix_transport
