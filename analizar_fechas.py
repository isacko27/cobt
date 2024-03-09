import os
import shutil
from openpyxl import load_workbook
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from globalv import *

class AnalizadorFechas():
    def __init__(self, citas_folder="citas", update_folder="citas/update"):
        self.citas_folder = citas_folder
        self.update_folder = update_folder
        self.email_sender = 'hervosoisaac@gmail.com'
        self.email_password = 'wptl madg hrjo yfwt'
        self.email_receivers = email_receivers

    def leer_fechas_excel(self, file_path):
        try:
            fechas = []
            workbook = load_workbook(filename=file_path)
            sheet = workbook.active
            for row in sheet.iter_rows(values_only=True):
                fechas.extend(row)
            return fechas
        except Exception as e:
            print(f"Error al leer fechas del archivo {file_path}: {e}")
            return []

    def enviar_correo(self, subject, body, sede):
        try:
            # Configurar el servidor SMTP de Gmail
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.email_sender, self.email_password)

            # Crear mensaje en formato HTML
            msg = MIMEMultipart()
            msg['From'] = self.email_sender
            msg['Subject'] = subject

            # Estilos CSS para el botón
            button_style = "background-color: #4CAF50; color: white; padding: 12px 20px; border: none; border-radius: 4px; cursor: pointer; text-decoration: none;"

            # Adjuntar cuerpo del mensaje como HTML
            mensaje_html = f"""
                    <html>
                        <head></head>
                        <body>
                            <h2>Se encontraron citas extraordinarias en la sede: {sede}</h2>
                            <p>{body}</p>
                            <form action="https://servicios.educacionvial.go.cr/Formularios/IngresarCuenta">
                                <input type="submit" value="Ir a COSEVI" style="{button_style}">
                            </form>
                        </body>
                    </html>
                    """
            msg.attach(MIMEText(mensaje_html, 'html'))

            # Agregar destinatarios al campo "To"
            msg['To'] = ', '.join(self.email_receivers)

            # Enviar correo electrónico
            server.sendmail(self.email_sender, self.email_receivers, msg.as_string())

            print("Correo electrónico enviado exitosamente.")

            # Cerrar conexión
            server.quit()
        except Exception as e:
            print(f"Error al enviar correo electrónico: {e}")

    def enviar_correo_prueba(self):
        try:
            subject = "Prueba de Correo Electrónico"
            body = "Este es un correo de prueba enviado desde el Analizador de Fechas."
            sede = "Sede de Prueba"

            self.enviar_correo(subject, body, sede)
        except Exception as e:
            print(f"Error al enviar correo de prueba: {e}")

    def reemplazar_archivos(self):
        try:
            for filename in os.listdir(self.update_folder):
                if filename.endswith(".xlsx"):
                    update_path = os.path.join(self.update_folder, filename)
                    citas_path = os.path.join(self.citas_folder, filename)

                    print(f"Analizando el archivo {filename} en la carpeta 'update'...")

                    fechas_update = self.leer_fechas_excel(update_path)

                    if os.path.exists(citas_path):
                        fechas_citas = self.leer_fechas_excel(citas_path)

                        if fechas_update != fechas_citas:
                            print(f"El archivo {filename} en 'update' es diferente al de 'citas'.")
                            sede = filename.split("_")[0].upper()
                            fechas_nuevas = [fecha for fecha in fechas_citas if fecha not in fechas_update]
                            if fechas_nuevas:
                                mensaje = f"Nuevas citas extraordinarias en {sede}:<br>"
                                for fecha in fechas_nuevas:
                                    mensaje += f"- {fecha}<br>"
                                self.enviar_correo(f"({tipo_cita}) {sede} Nuevas citas extraordinarias", mensaje, sede)
                            else:
                                print("No se encontraron citas extraordinarias nuevas.")
                        else:
                            print(f"El archivo {filename} en 'update' es igual al de 'citas'.")
                    else:
                        print(f"No se encontró el archivo {filename} en la carpeta 'citas'.")

            # Copiar archivos de citas a update
            for filename in os.listdir(self.citas_folder):
                if filename.endswith(".xlsx"):
                    citas_path = os.path.join(self.citas_folder, filename)
                    update_path = os.path.join(self.update_folder, filename)

                    # Si el archivo ya existe en update, no lo copiamos nuevamente
                    if not os.path.exists(update_path):
                        shutil.copy(citas_path, update_path)  # Copiar de citas a update
                        print(f"Archivo {filename} copiado de 'citas' a 'update'.")

        except Exception as e:
            print(f"Error al reemplazar archivos: {e}")

    def contenido_diferente(self, file1, file2):
        # Función para verificar si el contenido de dos archivos es diferente
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            return f1.read() != f2.read()

    def actualizar_carpeta_update(self):
        try:
            # Copiar archivos de citas a update
            for filename in os.listdir(self.citas_folder):
                if filename.endswith(".xlsx"):
                    citas_path = os.path.join(self.citas_folder, filename)
                    update_path = os.path.join(self.update_folder, filename)

                    shutil.copy(citas_path, update_path)  # Copiar de citas a update
                    print(f"Archivo {filename} copiado de 'citas' a 'update'.")
            print("La carpeta 'update' ha sido actualizada exitosamente.")
        except Exception as e:
            print(f"Error al actualizar la carpeta 'update': {e}")


# Uso de la clase AnalizadorFechas
analizador = AnalizadorFechas()
analizador.reemplazar_archivos()
analizador.actualizar_carpeta_update()
