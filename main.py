from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pyautogui
import time
from PIL import ImageGrab
from functools import partial


ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

service = Service("chromedriver.exe")
options = webdriver.ChromeOptions()
#options.add_extension("helium10.crx")
options.add_argument(r"user-data-dir=C:\Users\fisch\AppData\Local\Google\Chrome\User Data\Profile 1")
options.add_argument("start-maximized")
#options.add_argument("disable-infobars")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://google.com")

time.sleep(1)

def open_extension():
    # x, y = pyautogui.locateOnScreen(r"images\extensions_pic.png")
    # pyautogui.click(x, y)
    # time.sleep(1)
    x, y = pyautogui.locateOnScreen(r"images\helium_picture.jpg")
    pyautogui.click(x, y)


open_extension()

time.sleep(2)

driver.quit()
