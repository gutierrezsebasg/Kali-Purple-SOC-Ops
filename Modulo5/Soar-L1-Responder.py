#!/usr/bin/env python3
import re
import os
from collections import Counter

FAILED_AUTH_PATTERN = r"Failed password for .* from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
UMBRAL_ALERTA = 3

def analizar_logs(log_path="prueba_log.txt"):
    if not os.path.exists(log_path):
        print(f"[!] El archivo de log no existe.")
        return
    print(f"[*] Leyendo el archivo de log...")
    with open(log_path, 'r', errors='ignore') as f:
        contenido = f.read()

    ips_encontradas = re.findall(FAILED_AUTH_PATTERN, contenido)
    conteo_ips = Counter(ips_encontradas)

    print("\n[+] Resultados del analisis:")
    for ip, cantidad in conteo_ips.items():
        if cantidad >= UMBRAL_ALERTA:
            print(f"    ALERTA: IP sospechosa: {ip} ({cantidad} intentos fallidos)")
            print(f"    [ACCION SOAR L1]: sudo ufw deny from {ip} to any")
        else:
            print(f"    IP en observacion: {ip} ({cantidad} intentos)")

if __name__ == "__main__":
    analizar_logs()
