import time
from cosevi_bot import CoseviBot
from analizar_fechas import AnalizadorFechas
from globalv import *
from bypass import Bypass


bypass_instance = Bypass()
analizador = AnalizadorFechas()

# Inicia sesión en Google
#bypass_instance.google_login(gemail, gpasswd)
bypass_instance.google_login_debug()
driver = bypass_instance.get_driver()  # Obtener el controlador desde Bypass
# Crea una instancia de CoseviBot y pasa el controlador
bot = CoseviBot(driver)

while True:
    try:

        # Iniciando Sesion en Cosevi
        bot.IniciarSesion(cedula, password, tipo_identificacion)
        bot.ingresarRecibo(num_recibo, tipo_cita)
        bot.consultarCede("PASO ANCHO (EDUCACION VIAL)")
        bot.consultarCede("ALAJUELA")
        bot.consultarCede("CARTAGO")
        bot.consultarCede("GUAPILES")
        bot.consultarCede("HEREDIA")
        bot.consultarCede("LIBERIA")
        # bot.consultarCede("LIMON")
        # bot.consultarCede("NICOYA")
        # bot.consultarCede("PEREZ ZELEDON")
        # bot.consultarCede("PUNTARENAS")
        # bot.consultarCede("RIO CLARO")
        bot.consultarCede("SAN CARLOS")
        bot.consultarCede("SAN RAMON")
        bot.cerrar_sesion()
        bot.Restart()

        print(f"""=================================
Esperando {interbalo / 60} minutos para volver a intentar
=================================""")
        time.sleep(interbalo)

    except Exception as e:
        print(f"Se produjo un error: {e}")
        analizador.enviar_correo_error()
        print("Reiniciando el proceso...")
        bot.Restart()
