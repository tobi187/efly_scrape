import PySimpleGUI as sg

layout = [
    [sg.Text("Helium Automation"), sg.Button(
        "WebConfig", key="web"), sg.Button("Einstellungen")],
    [sg.Text('Filename')],
    [sg.Input("", key="file"), sg.FileBrowse()],
    [sg.OK(key="Start"), sg.Cancel()]
]


login_layout = [
    [sg.Text("Helium10 LoginFehler")],
    [sg.Text("Leider wurde deine Einlogdaten gelöscht, bitte gib sie neu ein")],
    [sg.Text("Email: "), sg.Input("", key="user")],
    [sg.Text("Passwort: "), sg.Input("", key="pass")],
    [sg.Text("Wenn du auf Ok drückst wird die Automatiesierung sofort gestartet")],
    [sg.Ok(key="Login"), sg.Cancel()]
]
