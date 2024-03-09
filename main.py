from undetected_chromedriver import Chrome, ChromeOptions
import time
from cosevi_bot import CoseviBot
from analizar_fechas import AnalizadorFechas
from globalv import *
from bypass import Bypass


# Inicia sesión en Google
bypass_instance = Bypass()
bypass_instance.google_login(gemail, gpasswd)
driver = bypass_instance.driver  # Usa el mismo driver de Bypass

# Crea una instancia de CoseviBot y pasa el driver
bot = CoseviBot(driver)

while True:
    try:
        # bot.debug()
        bot.IniciarSesion(cedula, password)
        bot.ingresarRecibo(num_recibo, tipo_cita)
        bot.consultarCede("PASO ANCHO (EDUCACION VIAL)")
        bot.consultarCede("ALAJUELA")
        bot.consultarCede("CARTAGO")
        bot.consultarCede("GUAPILES")
        bot.consultarCede("RIO CLARO")
        bot.consultarCede("HEREDIA")
        bot.consultarCede("SAN RAMON")
        bot.consultarCede("SAN CARLOS")

        analizador = AnalizadorFechas()
        analizador.reemplazar_archivos()
        analizador.actualizar_carpeta_update()

        print(f"""=================================
Esperando {interbalo / 60} minutos para volver a intentar
=================================""")
        time.sleep(interbalo)

    except Exception as e:
        print(f"Se produjo un error: {e}")
        print("Reiniciando el proceso...")
        bot.CerrarSesion()
