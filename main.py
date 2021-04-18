# from ad import *

import PySimpleGUI as sg
import pandas as pd

from alfabeta import *
from cycles import *
from calculations import *

# Add your new theme colors and settings
my_new_theme = {'BACKGROUND': '#709053',
                'TEXT': '#fff4c9',
                'INPUT': '#c7e78b',
                'TEXT_INPUT': '#000000',
                'SCROLL': '#c7e78b',
                'BUTTON': ('white', '#709053'),
                'PROGRESS': ('#01826B', '#D0D0D0'),
                'BORDER': 1,
                'SLIDER_DEPTH': 0,
                'PROGRESS_DEPTH': 0}

# Add your dictionary to the PySimpleGUI themes
sg.theme_add_new('MyNewTheme', my_new_theme)

# Switch your theme to use the newly added one. You can add spaces to make it more readable
sg.theme('My New Theme')


# Update function
def update(popyt, podaz):
    text_elem_3 = window['-text3-']
    text_elem_4 = window['-text4-']
    text_elem_4.update(f"POPYT: {popyt}")
    text_elem_3.update(f"PODAŻ: {podaz}")


def str_to_float(values):
    return {k: float(v) for k, v in values.items() if k not in ["-profitmatrix-", "-finalmatrix-"]}


def matrixs(tab):
    size1 = 2
    size2 = 2
    arr = np.array(tab).reshape(size1, size2)
    return arr


basic_matrix = np.zeros((3, 3))
basic_table = pd.DataFrame(data=basic_matrix, columns=["O1", "O2", "OF"])
basic_table["D/O"] = ["D1", "D2", "DF"]
basic_table = basic_table[["D/O", "O1", "O2", "OF"]]
basic_list = basic_table.values.tolist()

# Define the window's contents i.e. layout
layout = [[sg.Text('PODAŻ:', size=(17, 1), key='-text1-', font='Helvetica 16'),
           sg.In("10", size=(20, 25), enable_events=True, key="-podaz1-"),
           sg.In("28", size=(20, 25), enable_events=True, key="-podaz2-")],

          [sg.Text('POPYT:', size=(17, 1), key='-text2-', font='Helvetica 16'),
           sg.In("20", size=(20, 25), enable_events=True, key="-popyt1-"),
           sg.In("30", size=(20, 25), enable_events=True, key="-popyt2-")],

          [sg.Text('KOSZT ZAKUPU:', size=(17, 1), key='-text3-', font='Helvetica 16'),
           sg.In("10", size=(20, 25), enable_events=True, key="-kosztzakupu1-"),
           sg.In("12", size=(20, 25), enable_events=True, key="-kosztzakupu2-")],

          [sg.Text('CENA SPRZEDAŻY:', size=(17, 1), key='-text4-', font='Helvetica 16'),
           sg.In("30", size=(20, 25), enable_events=True, key="-cenasprzedazy1-"),
           sg.In("25", size=(20, 25), enable_events=True, key="-cenasprzedazy2-")],
          [sg.Text('\nKOSZTY TRANSPORTU:', size=(25, 2), key='-text5-', font='Helvetica 16')],
          [sg.In("8", size=(20, 25), enable_events=True, key="-kosztytransportu1-"),
           sg.In("14", size=(20, 25), enable_events=True, key="-kosztytransportu2-")],
          [sg.In("12", size=(20, 25), enable_events=True, key="-kosztytransportu3-"),
           sg.In("9", size=(20, 25), enable_events=True, key="-kosztytransportu4-")],

          [sg.Button('OBLICZ', enable_events=True, key='-Button2-', font='Helvetica 16')],

          [sg.Text('\nWYNIKI\n', size=(43, 2), key='-te-', font='Helvetica 16', justification="center")],
            [sg.Text('ZYSKI:', size=(25, 1), key='-text5-', font='Helvetica 16')],

          [sg.Table(values=basic_list, headings=list(basic_table.columns), font='Helvetica',
                    display_row_numbers=False,
                    hide_vertical_scroll=True,
                    auto_size_columns=False,
                    num_rows=3, key='-profitmatrix-', justification="center")],

          [sg.Text('\nOPTYMALNY PRZEJAZD:', size=(25, 2), key='-text5-', font='Helvetica 16')],
          [sg.Table(values=basic_list, headings=list(basic_table.columns), font='Helvetica',
                    display_row_numbers=False,
                    hide_vertical_scroll=True,
                    auto_size_columns=False,
                    num_rows=3, key='-finalmatrix-', justification="center")],
          [sg.Text('KOSZTY:', size=(17, 1), key='-text10-', font='Helvetica 16'),
            sg.Text('', size=(17, 1), key='-KOSZTY-', font='Helvetica 16')],
          [sg.Text('ZYSKI:', size=(17, 1), key='-text11-', font='Helvetica 16'),
            sg.Text('', size=(17, 1), key='-ZYSKI-', font='Helvetica 16')],
          [sg.Text('ZYSKI KOŃCOWE:', size=(17, 1), key='-text12-', font='Helvetica 16'),
            sg.Text('', size=(17, 1), key='-KONCOWEZYSKI-', font='Helvetica 16')],
          ]


# Create the window


window = sg.Window('Zagadnienie pośrednika', layout)  # size=(350, 300)

# Event loop
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == '-Button-':
        update(values["-popyt-"], values["-podaz-"])
    if event == "-Button2-":
        print(values)
        try:

            valuesint = str_to_float(values)
            matrix_selling_cost = (matrixs(
                [valuesint["-cenasprzedazy1-"], valuesint["-cenasprzedazy2-"], valuesint["-cenasprzedazy1-"],
                 valuesint["-cenasprzedazy2-"]]))
            matrix_cost_buy = (matrixs(
                [valuesint["-kosztzakupu1-"], valuesint["-kosztzakupu1-"], valuesint["-kosztzakupu2-"],
                 valuesint["-kosztzakupu2-"]]))
            matrix_cost_trans = (matrixs(
                [valuesint["-kosztytransportu1-"], valuesint["-kosztytransportu2-"], valuesint["-kosztytransportu3-"],
                 valuesint["-kosztytransportu4-"]]))
            matrix_profits = matrix_selling_cost - matrix_cost_buy - matrix_cost_trans
            matrix_zeros = basic_table.to_numpy()
            matrix_zeros[:-1, 1:-1] = matrix_profits
            window.Element("-profitmatrix-").Update(values=pd.DataFrame(data=matrix_zeros).values.tolist())

            matrix_demand = [valuesint["-popyt1-"], valuesint["-popyt2-"], sum([valuesint["-podaz1-"], valuesint["-podaz2-"]])]

            matrix_supply = [valuesint["-podaz1-"], valuesint["-podaz2-"], sum([valuesint["-popyt1-"], valuesint["-popyt2-"]])]

        except Exception as error:
            print(error)
            sg.popup_error("Podaj liczbe")

        matrix_profit = np.zeros((3, 3))
        matrix_profit[:-1, :-1] = matrix_profits

        matrix_selling_costs = np.zeros((3, 3))
        matrix_selling_costs[:-1, :-1] = matrix_selling_cost

        matrix_cost_buys = np.zeros((3, 3))
        matrix_cost_buys[:-1, :-1] = matrix_cost_buy

        matrix_cost_transport = np.zeros((3, 3))
        matrix_cost_transport[:-1, :-1] = matrix_cost_trans

        matrix_transport, ending_profit, whole_profit, whole_cost = final_calculation(matrix_supply, matrix_demand, matrix_profit, matrix_selling_costs, matrix_cost_buys, matrix_cost_transport)

        matrix_zeros = basic_table.to_numpy()
        matrix_zeros[:, 1:] = matrix_transport

        window.Element("-finalmatrix-").Update(values=pd.DataFrame(data=matrix_zeros).values.tolist())
        window.Element("-KOSZTY-").Update(whole_cost)
        window.Element("-ZYSKI-").Update(whole_profit)
        window.Element("-KONCOWEZYSKI-").Update(ending_profit)



# Close the window i.e. release resource
window.close()
