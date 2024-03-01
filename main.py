import time
from cosevi_bot import CoseviBot
from analizar_fechas import AnalizadorFechas
from globalv import *

# Define global variables

while True:
    bot = CoseviBot()
    analizador = AnalizadorFechas(tipo_cita)
    try:
        bot.IniciarSesion(cedula, password)
        bot.ingresarRecibo(num_recibo, tipo_cita)
        bot.consultarCede("PASO ANCHO (EDUCACION VIAL)")
        bot.consultarCede("ALAJUELA")
        bot.consultarCede("CARTAGO")
        # bot.consultarCede("GUAPILES")
        bot.consultarCede("HEREDIA")
        # bot.consultarCede("LIMON")
        # bot.consultarCede("LIBERIA")
        bot.consultarCede("SAN RAMON")
        bot.consultarCede("SAN CARLOS")
        # bot.consultarCede("PUNTARENAS")
        # bot.consultarCede("PEREZ ZELEDON")
        # bot.consultarCede("NICOYA")
        bot.CerrarSesion()

        analizador.reemplazar_archivos()  # Pass tipo_cita as an argument
        analizador.actualizar_carpeta_update()
        # Esperar 6 horas antes de ejecutar nuevamente el bot
        print("""=================================
Esperando 30 minutos para volver a intentar
=================================""")
        time.sleep(30 * 60)  # 6 horas en segundos

    except Exception as e:
        print(f"Se produjo un error: {e}")
        print("Reiniciando el proceso...")
        bot.CerrarSesion()  # Cerrar el driver actual
        bot = CoseviBot()   # Crear una nueva instancia de CoseviBot