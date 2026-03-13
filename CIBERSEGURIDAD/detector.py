import os
import subprocess
import re 


# Mensaje inicial
print("=== DETECTOR DE DISPOSITIVOS POR IP ===")

ip_usuario = input("Ingrese la dirección IP o el rango de IPs a escanear (ejemplo: 192.168.1.1 o 192.168.1.1-100): ")
resultado = subprocess.run(["ping", "-n", "1", ip_usuario], capture_output=True, text=True)

salida = resultado.stdout

if "TTL=" in salida:

    print(f"La ip {ip_usuario} está activa.")     

    # Buscar TTL en regex
    ttl = re.search(r"TTL=(\d+)", salida)

    if ttl:
        ttl_valor = int(ttl.group(1))
        print("TTL detectado:", ttl_valor)
        if ttl_valor >= 200:
            tipo = "Router o dispositivo de red"
        elif ttl_valor >= 120:
            tipo = "Computadora (Windows)"
        elif ttl_valor >= 60:
            tipo = "Linux/ Android / Celular / Router basado en Linux"
        else:
            tipo = "Dispositivo desconocido"
        
        print("Tipo de dispositivo estimado:", tipo)

else:
    print("La IP no responde. Puede estar inactiva o bloqueando pings.")