import time
from cosevi_bot import CoseviBot
from analizar_fechas import AnalizadorFechas


while True:
    bot = CoseviBot()
    analizador = AnalizadorFechas()
    try:
        bot.IniciarSesion("118910588", "Pascal2$")
        bot.ingresarRecibo("3258970209", "A2")
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

        analizador.reemplazar_archivos()
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
