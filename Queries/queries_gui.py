from worldometer import worldometer_menu


worldometer_menu.generate_files("./worldometers_countrylist.txt")

from module_1 import query_1
from module_2 import query_2
from module_3_1 import query_3
import PySimpleGUI as sg


# GUI Layout
layout = [
    [sg.Button('Query Worldometer'), sg.Button('Query Wikipedia')],
    [sg.Text(size=(60,2), key='-OUTPUT-')],
    [sg.Exit()]
]

# Create the Window
window = sg.Window('Data Extraction', layout)

window.close()