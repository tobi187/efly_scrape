from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyperclip
import pyautogui
import time

CONFIDENCE = 0.7


class AutoWorker():
    def __init__(self) -> None:
        self.driver = self.configure()

    def configure(self):
        service = Service("chromedriver.exe")
        options = webdriver.ChromeOptions()
        options.add_argument(
            r"user-data-dir=C:\Users\fisch\AppData\Local\Google\Chrome\User Data\Profile 1")
        options.add_argument("start-maximized")
        # options.add_argument("disable-infobars")
        return webdriver.Chrome(service=service, options=options)

    def get_total_rev(self, url, long=False) -> str:
        if long:
            pause = 10
        else:
            pause = 2

        self.driver.get(url)

        time.sleep(100)

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
                return "False"

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

    def test_if_logged_in(self) -> bool:
        login_url = "https://members.helium10.com/user/signin"
        self.driver.get(login_url)
        time.sleep(2)
        current_url = self.driver.current_url
        self.driver.quit()
        return current_url != login_url

    def login(self, username, password) -> bool:
        self.driver.get("https://members.helium10.com/user/signin")
        user_input_id = "loginform-email"  # name: LoginForm[email]
        pass_input_id = "loginform-password"  # name: LoginForm[password]
        user_el = self.driver.find_element(by=By.ID, value=user_input_id)
        pass_el = self.driver.find_element(by=By.ID, value=pass_input_id)

        user_el.send_keys(username)
        pass_el.send_keys(password)
        self.driver.send_keys(Keys.ENTER)
        time.sleep(2)
        return self.driver.get("https://members.helium10.com/user/signin") == "https://members.helium10.com/user/signin"
