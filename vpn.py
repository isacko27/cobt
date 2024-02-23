import os
import subprocess

# Lista de servidores VPN gratuitos
SERVIDORES_VPN = {
    "OpenVPN": {
        "servidor": "vpn.example.com",
        "usuario": "usuario",
        "contrasena": "contrasena",
        "archivo_conf": "openvpn.conf"
    },
    "WireGuard": {
        "servidor": "wg.example.com",
        "puerto": "51820",
        "clave_publica": "clave_publica.wg",
        "clave_privada": "clave_privada.wg"
    }
}

# Seleccionar el tipo de VPN
tipo_vpn = input("Seleccione el tipo de VPN (OpenVPN/WireGuard): ").lower()

# Validar la selección
if tipo_vpn not in SERVIDORES_VPN:
    print(f"Error: Tipo de VPN '{tipo_vpn}' no válido.")
    exit()

# Obtener los datos del servidor
servidor = SERVIDORES_VPN[tipo_vpn]["servidor"]
usuario = SERVIDORES_VPN[tipo_vpn].get("usuario")
contrasena = SERVIDORES_VPN[tipo_vpn].get("contrasena")
archivo_conf = SERVIDORES_VPN[tipo_vpn].get("archivo_conf")
puerto = SERVIDORES_VPN[tipo_vpn].get("puerto")
clave_publica = SERVIDORES_VPN[tipo_vpn].get("clave_publica")
clave_privada = SERVIDORES_VPN[tipo_vpn].get("clave_privada")

# Conectarse a la VPN
if tipo_vpn == "openvpn":
    comando = ["openvpn", "--config", archivo_conf, "--auth-user-pass"]
    if usuario and contrasena:
        comando.append(f"{usuario}:{contrasena}")
    subprocess.run(comando)
elif tipo_vpn == "wireguard":
    comando = ["wg-quick", "up", f"{servidor}:{puerto}", "--private-key={clave_privada}", "--public-key={clave_publica}"]
    subprocess.run(comando)

# Mostrar mensaje de éxito
print("¡Conectado a la VPN con éxito!")

# Desconectarse de la VPN (opcional)
def desconectar_vpn():
    if tipo_vpn == "openvpn":
        comando = ["killall", "openvpn"]
    elif tipo_vpn == "wireguard":
        comando = ["wg-quick", "down", f"{servidor}:{puerto}"]
    subprocess.run(comando)

# Opción para desconectarse
opcion = input("¿Desea desconectarse de la VPN? (s/n): ").lower()
if opcion == "s":
    desconectar_vpn()