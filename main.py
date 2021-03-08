from ad import *

import PySimpleGUI as sg
import numpy as np

# Update function
def update(popyt, podaz):
    text_elem_3 = window['-text3-']
    text_elem_4 = window['-text4-']
    text_elem_4.update(f"POPYT {popyt}")
    text_elem_3.update(f"PODAŻ {podaz}")

def sum():
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




# Define the window's contents i.e. layout
layout = [[sg.Text('PODAŻ:', size=(25, 1), key='-text1-', font='Helvetica 16'),
           sg.In(size=(25, 25), enable_events=True, key="-podaz-")],
          [sg.Text('POPYT:', size=(25, 1), key='-text2-', font='Helvetica 16'),
           sg.In(size=(25, 25), enable_events=True, key="-popyt-")],
          [sg.Button('Ok', enable_events=True, key='-Button-', font='Helvetica 16')],
        [sg.Text('POPYT', size=(25, 1), key='-text3-', font='Helvetica 16'),
        sg.Text('POPYT', size=(25, 1), key='-text4-', font='Helvetica 16')],
        [sg.Text('SUMA: ', size=(25, 1), key='-text5-', font='Helvetica 16'),
         sg.Button('SHOW', enable_events=True, key='-Button2-', font='Helvetica 16')]
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
        sum()

# Close the window i.e. release resource
window.close()