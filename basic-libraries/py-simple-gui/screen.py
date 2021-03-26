import PySimpleGUI as sg
import datetime as time

date = time.datetime.now()
current_time = date.strftime("%H:%M:%S").split(':')
print(current_time)

layout = [[sg.Text("Qual seu nome?")], [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40, 1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Sair')]]

window = sg.Window('Nome', layout)
while True:
    event, values = window.read()
    print(f"{values['-INPUT-']}: {event}")
    if sg.WINDOW_CLOSED or event == 'Sair':
        break
    if 12 < int(current_time[0]) < 18:
        window['-OUTPUT-'].update('Opa ' + values['-INPUT-'] + "! Boa tarde!")
    elif 4 < int(current_time[0]) <= 12:
        window['-OUTPUT-'].update('Opa ' + values['-INPUT-'] + "! Bom dia!")
    else:
        window['-OUTPUT-'].update('Opa ' + values['-INPUT-'] + "! Boa noite!")
