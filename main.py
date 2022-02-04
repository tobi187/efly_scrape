import time
from screen import layout, login_layout
import PySimpleGUI as sg
from worker import AutoWorker
from excel_stuff import save_data, get_data
from datetime import datetime


def action():
    window = sg.Window("Helium Automation", layout)
    event, values = window.read()
    while True:
        if event == sg.WINDOW_CLOSED:
            window.close()
            break
        if event == "Cancel":
            window.close()
            break
        if event == "Testen":
            test_res = AutoWorker().test_confidence("https://www.amazon.de/-/en/s?ie=UTF8&marketplaceID=A1PA6795UKMFR9&me=A2Y45U1SJYRN75")
            print(test_res)
            time.sleep(2)
            continue

        if event == "Start":
            worker = AutoWorker()
            # user_he = ""
            # pass_he = ""
            win2 = sg.Window("Login", login_layout)
            ev2, val2 = win2.read()
            while True:
                if ev2 == sg.WINDOW_CLOSED:
                    exit()
                if ev2 == "Cancel":
                    exit()
                if ev2 == "Login":
                    user_he = val2["user"]
                    pass_he = val2["pass"]
                    if worker.login(user_he, pass_he):
                        win2.close()
                        break
                    else:
                        sg.PopupError("Sorry etwas hat nicht funktioniert")
                        exit()
            urls, row_nr, path, total_len = get_data(values["file"])
            start_time = datetime.now()
            print(urls)
            total_revs = []
            worker.activate()
            for index, li in enumerate(urls):
                if index % 49 == 0:
                    worker.login(user_he, pass_he)

                res = worker.get_total_rev(li)
                if res == "0":
                    res = worker.get_total_rev(li, long=True)
                total_revs.append(res)
            worker.deactivate()
            print(total_revs)
            save_data(path, row_nr, total_revs, total_len)
            total_time = datetime.now() - start_time
            sg.PopupOK(
                f"Fertig. Benötigte Zeit: {total_time.seconds // 3600} Stunden und {(total_time.seconds // 60) % 60} Minuten bei {len(urls)} Links")
            exit()
