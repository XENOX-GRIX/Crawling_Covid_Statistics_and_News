import PySimpleGUI as sg
from ".worldometer" worldometer_menu

worldometer_menu.menu()
# Example Menu Functions
def function1():
    sg.popup('Function 1 Called', 'More details about function 1.')

def function2():
    sg.popup('Function 2 Called', 'More details about function 2.')

# Define the layout
layout = [
    [sg.Text('Menu Driven GUI', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    [sg.Button('Function 1'), sg.Button('Function 2')],
    [sg.Exit()]
]

# Create the Window
window = sg.Window('My Menu Driven GUI', layout)

# Event Loop
while True:
    event, values = window.read()
    if event in (None, 'Exit'):  # if user closes window or clicks exit
        break
    elif event == 'Function 1':
        function1()
    elif event == 'Function 2':
        function2()

# Close the Window
window.close()
