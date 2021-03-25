#from ad import *

import PySimpleGUI as sg
import numpy as np

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

def suma():
    number = 100

    suma = 0
    for i in range(number):
        suma += i

    text_elem_4 = window['-text5-']
    text_elem_4.update(f"{suma}")

    while suma > 80:
        suma -= 4

    text_elem_4 = window['-text5-']
    text_elem_4.update(f"{suma}")


def str_to_float(values):
    return {k: float(v) for k, v in values.items()}

def matrixs(tab):
    size1 = 2
    size2 = 2
    arr = np.array(tab).reshape(size1, size2)
    return arr


# Define the window's contents i.e. layout
layout = [[sg.Text('PODAŻ:', size=(17, 1), key='-text1-', font='Helvetica 16'),
           sg.In("10", size=(25, 25), enable_events=True, key="-podaz1-"),
           sg.In("28", size=(25, 25), enable_events=True, key="-podaz2-")],

            [sg.Text('POPYT:', size=(17, 1), key='-text2-', font='Helvetica 16'),
           sg.In("20", size=(25, 25), enable_events=True, key="-popyt1-"),
           sg.In("30", size=(25, 25), enable_events=True, key="-popyt2-")],

            [sg.Text('KOSZT ZAKUPU:', size=(17, 1), key='-text3-', font='Helvetica 16'),
           sg.In("10", size=(25, 25), enable_events=True, key="-kosztzakupu1-"),
           sg.In("12", size=(25, 25), enable_events=True, key="-kosztzakupu2-")],

            [sg.Text('CENA SPRZEDAŻY:', size=(17, 1), key='-text4-', font='Helvetica 16'),
           sg.In("30", size=(25, 25), enable_events=True, key="-cenasprzedazy1-"),
           sg.In("25", size=(25, 25), enable_events=True, key="-cenasprzedazy2-")],
          [sg.Text('\nKOSZTY TRANSPORTU:', size=(25, 2), key='-text5-', font='Helvetica 16')],
          [sg.In("8", size=(25, 25), enable_events=True, key="-kosztytransportu1-"),
           sg.In("14", size=(25, 25), enable_events=True, key="-kosztytransportu2-")],
          [sg.In("12", size=(25, 25), enable_events=True, key="-kosztytransportu3-"),
           sg.In("9", size=(25, 25), enable_events=True, key="-kosztytransportu4-")],

          [sg.Button('Ok', enable_events=True, key='-Button-', font='Helvetica 16')],
        [sg.Button('KONWERTER', enable_events=True, key='-Button2-', font='Helvetica 16')]
          ]

# Create the window


window = sg.Window('Zagadnienie pośrednika', layout) #size=(350, 300)

# Event loop
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == '-Button-':
        update(values["-popyt-"], values["-podaz-"])
    if event == "-Button2-":
        values = str_to_float(values)
        matrix_selling_cost = (matrixs([values["-cenasprzedazy1-"], values["-cenasprzedazy2-"], values["-cenasprzedazy1-"],values["-cenasprzedazy2-"]]))
        matrix_cost_buy = (matrixs([values["-kosztzakupu1-"], values["-kosztzakupu1-"], values["-kosztzakupu2-"],values["-kosztzakupu2-"]]))
        matrix_cost_trans = (matrixs([values["-kosztytransportu1-"], values["-kosztytransportu2-"], values["-kosztytransportu3-"],values["-kosztytransportu4-"]]))
        matrix_profits=matrix_selling_cost-matrix_cost_buy-matrix_cost_trans
        print(matrix_profits)

# Close the window i.e. release resource
window.close()

