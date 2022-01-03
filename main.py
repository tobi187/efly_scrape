from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pyautogui
import time
from bs4 import BeautifulSoup


service = Service("chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument(
    r"user-data-dir=C:\Users\fisch\AppData\Local\Google\Chrome\User Data\Profile 1")
options.add_argument("start-maximized")
# options.add_argument("disable-infobars")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.amazon.de/s?me=A1E8NY3N6ZZMFX&marketplaceID=A1PA6795UKMFR9")

time.sleep(3)


def open_extension():
    # x, y = pyautogui.locateOnScreen(r"images\extensions_pic.png")
    # pyautogui.click(x, y)
    # time.sleep(1)
    x, y, _, _ = pyautogui.locateOnScreen(
        r"images\helium_picture.jpg", confidence=0.3)
    pyautogui.click(x + 10, y + 10)
    time.sleep(2)
    x, y, _, _ = pyautogui.locateOnScreen(
        r"images\xray_only.png", confidence=0.3)
    pyautogui.click(x, y)
    time.sleep(2)
    # x, y, _, _ = pyautogui.locateOnScreen(r"download_icon.png", confidence=0.8)
    # pyautogui.click(x, y)


open_extension()

driver.switch_to.active_element()

el = driver.find_element_by_xpath(
    "/html/body/div[2]/div//div/div/div/div[2]/div[2]/div[1]/h2")

print(el)
