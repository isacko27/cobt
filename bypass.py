from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random
import os
from selenium_stealth import stealth


from seleniumbase import SB

class Bypass:
    def __init__(self):
        self.email = ""
        self.password = ""

    def google_login(self, google_email, google_password):
        self.email = google_email
        self.password = google_password

        with SB(uc=True) as sb:
            sb.open("https://www.google.com/gmail/about/")
            sb.click('a[data-action="sign in"]')
            sb.type('input[type="email"]', self.email)
            sb.click('button:contains("Next")')
            sb.sleep(5)
            sb.type('input[type="password"]', self.password)
            sb.click('button:contains("Next")')

    def close_driver(self):
        pass
