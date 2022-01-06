from screen import layout, login_layout
import PySimpleGUI as sg
from worker import AutoWorker

link = "https://www.amazon.de/s?k=babywalz&ref=bl_dp_s_web_7096167031"


# def get_links():
#     output = []
#     wb = xw.Book.caller()
#     curr_sheet: Sheet = wb.sheets[1]
#     range: Range = curr_sheet.range("D1", "D100").value
#     for col in range:
#         if col == None or col == "":
#             curr_sheet.range("D1").options(TRANSPOSE=True).value = output

#         total_rev = get_total_rev(col)
#         if total_rev == "err":
#             total_rev = get_total_rev(col, long=True)

#         if total_rev != "err":
#             output.append(total_rev)
#         else:
#             output.append("something went wrong")


def action():
    window = sg.Window("Helium Automation", layout)
    event, values = window.read()
    while True:
        if event == sg.WINDOW_CLOSED:
            window.close()
            break
        if event == "OK":
            print(values[0])
            worker = AutoWorker()
            if not worker.test_if_logged_in():
                win2 = sg.Window("Login", login_layout)
                ev2, val2 = win2.read()
                while True:
                    if ev2 == sg.WINDOW_CLOSED:
                        exit()
                    if ev2 == "Cancel":
                        exit()
                    if ev2 == "OK":
                        user = val2["user"]
                        password = val2["pass"]
                        if worker.login(user, password):
                            win2.close()
                            break
                        else:
                            sg.PopupError("Sorry etwas hat nicht funtioniert")
                            exit()
                worker.get_total_rev()

            else:
                worker.get_total_rev()


if __name__ == "__main__":
    action()
