from PIL.Image import TRANSPOSE
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyperclip
import pyautogui
import time
import xlwings as xw
import numpy as np
from xlwings.main import Range, Sheet
from screen import layout
import PySimpleGUI as sg

CONFIDENCE = 0.7

# setup
service = Service("chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument(
    r"user-data-dir=C:\Users\fisch\AppData\Local\Google\Chrome\User Data\Default")
options.add_argument("start-maximized")
# options.add_argument("disable-infobars")
driver = webdriver.Chrome(service=service, options=options)


def get_total_rev(url, long=False):
    if long:
        pause = 10
    else:
        pause = 2

    driver.get(url)

    time.sleep(pause)

    try:
        x, y, _, _ = pyautogui.locateOnScreen(
            r"images\helium_pic.png", confidence=CONFIDENCE)
        pyautogui.click(x + 10, y + 10)
        time.sleep(pause)

        x, y, _, _ = pyautogui.locateOnScreen(
            r"images\xray_only.png", confidence=CONFIDENCE)
        pyautogui.click(x, y)
        time.sleep(pause)
    except TypeError:
        try:
            x, y, _, _ = pyautogui.locateOnScreen(
                r"images\helium_grey.png", confidence=CONFIDENCE)
            pyautogui.click(x + 10, y + 10)
            print("grey")
            time.sleep(pause)
        except TypeError:
            return False

    # open field to search on site, search total revenue,
    pyautogui.hotkey("ctrl", "f")
    time.sleep(.1)
    pyautogui.typewrite("TOTAL REVENUE")
    time.sleep(.5)
    pyautogui.hotkey("esc")
    time.sleep(.5)
    pyautogui.hotkey("shiftleft", "shiftright", "down")
    time.sleep(1)
    pyautogui.hotkey("ctrl", "c")
    time.sleep(.5)

    text = pyperclip.paste()
    return text.split("\n")[1]


link = "https://www.amazon.de/s?k=babywalz&ref=bl_dp_s_web_7096167031"


def get_links():
    output = []
    wb = xw.Book.caller()
    curr_sheet: Sheet = wb.sheets[1]
    range: Range = curr_sheet.range("D1", "D100").value
    for col in range:
        if col == None or col == "":
            curr_sheet.range("D1").options(TRANSPOSE=True).value = output

        total_rev = get_total_rev(col)
        if total_rev == "err":
            total_rev = get_total_rev(col, long=True)

        if total_rev != "err":
            output.append(total_rev)
        else:
            output.append("something went wrong")


def action():
    window = sg.Window("Helium Automation", layout)
    event, values = window.read()
    while True:
        if event == sg.WINDOW_CLOSED:
            window.close()
            break
        if event == "OK":
            print(values[0])
            print("output: " + get_total_rev(link))


if __name__ == "__main__":
    action()
