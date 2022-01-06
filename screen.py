import PySimpleGUI as sg

layout = [
    [sg.Text('Filename')],
    [sg.Input(), sg.FileBrowse()],
    [sg.OK(), sg.Cancel()]
]


login_layout = [
    [sg.Text("Helium10 LoginFehler")],
    [sg.Text("Leider wurde deine Einlogdaten gelöscht, bitte gib sie neu ein")],
    [sg.Text("Email: "), sg.Input("", key="user")],
    [sg.Text("Passwort: ", sg.Input("", key="pass"))],
    [sg.Text("Wenn du auf Ok drückst wird die Automatiesierung sofort gestartet")],
    [sg.Ok(), sg.Cancel()]
]
