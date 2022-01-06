import PySimpleGUI as sg

layout = [
    [sg.Text('Filename')],
    [sg.Input(), sg.FileBrowse()],
    [sg.OK(), sg.Cancel()]
]
