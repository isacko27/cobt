# Bypass.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from undetected_chromedriver import Chrome, ChromeOptions
import time
import os  # Agrega esta línea para importar el módulo os

class Bypass:
    def __init__(self):
        self.driver = self.create_driver()

    def create_driver(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        chrome_driver_path = os.path.join(current_dir, 'chromedriver.exe')

        options = ChromeOptions()
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-dev-shm-usage")

        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.109 Safari/537.36'
        options.add_argument(f"user-agent={user_agent}")

        driver = Chrome(options=options, executable_path=chrome_driver_path)
        return driver

    def google_login(self, email, password):
        with self.driver:
            self.driver.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fwww.google.com%2F&ec=GAZAmgQ&hl=es-419&ifkv=ATuJsjwnH3OLD9vlLKtIdfhwbX1YHm7TF6yholcsyqxWwt8sC4IAuYG5eA9op-b0TwDxdpHfM45d&passive=true&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-2012304954%3A1710104768041639&theme=glif")
            print("[+]Iniciando Sesion En Google")

            # Esperar a que aparezca el campo de entrada del email
            email_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "identifierId"))
            )

            # Escribir el email proporcionado
            email_input.send_keys(email)

            # Hacer clic en el botón "Siguiente"
            next_button = self.driver.find_element(By.XPATH, "//span[text()='Siguiente']")
            next_button.click()

            # Esperar a que aparezca el campo de entrada de la contraseña
            password_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "Passwd"))
            )

            # Escribir la contraseña proporcionada
            password_input.click()
            password_input.send_keys(password)

            # Hacer clic en el botón "Siguiente" para iniciar sesión
            next_button = self.driver.find_element(By.XPATH, "//span[text()='Siguiente']")
            time.sleep(1)
            next_button.click()

    def google_login_debug(self):
        with self.driver:
            self.driver.get(
                    "https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fwww.google.com%2F&ec=GAZAmgQ&hl=es-419&ifkv=ATuJsjwnH3OLD9vlLKtIdfhwbX1YHm7TF6yholcsyqxWwt8sC4IAuYG5eA9op-b0TwDxdpHfM45d&passive=true&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-2012304954%3A1710104768041639&theme=glif")
            print("[+]Iniciando Sesion En Google en debug, tienes 1 minuto para iniciar sesion manualmente")
            time.sleep(60)

    def close_driver(self):
        self.driver.quit()

    def get_driver(self):
        return self.driver
