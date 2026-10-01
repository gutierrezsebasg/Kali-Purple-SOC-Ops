# Kali-Purple-SOC-Ops

# Módulo 1: Despliegue, Auditoría y Verificación del Entorno Defensivo

## 1. Objetivo Práctico
Auditar la disponibilidad de la suite de herramientas defensivas en Kali Purple, resolver dependencias faltantes (Troubleshooting) y establecer la estación de trabajo de análisis SOC L1.

## 2. Auditoría y Aprovisionamiento de Binarios Defensivos

Comando inicial de verificación de herramientas: `which tshark ufw tcpdump`

Al detectar herramientas faltantes y conflictos de firmas en los repositorios por defecto, procedemos con el aprovisionamiento manual

Instalación de IDS y Firewall:
`sudo apt update` ,  `sudo apt install ufw -y`

Despliegue Forense de Volatility 3 (Vía GitHub): 
`git clone [https://github.com/volatilityfoundation/volatility3.git](https://github.com/volatilityfoundation/volatility3.git)` , `cd volatility3` , `python3 vol.py --help`

| Herramienta | Categoría NIST | Estado Post-Aprovisionamiento | Aplicación Operativa SOC L1 |
| :--- | :--- | :--- | :--- |
| **Tshark** | Detect | Verificado | Inspección y filtrado de capturas de red (.pcap) |
| **Tcpdump** | Detect | Verificado | Captura rápida de tráfico en interfaces de red |
| **Volatility 3** | Respond | Clonado (GitHub) | Análisis forense de volcados de memoria RAM |
| **UFW** | Protect | Instalado (apt) | Gestión de reglas de cortafuegos para contención |

## 3. Verificación de Captura en Vivo (Tshark)

Ejecución de prueba de captura directa en interfaz de red para validar el entorno de monitoreo:
```bash
sudo tshark -i any -c 10
```
Resultado de validación:
Salida en consola de los primeros 10 paquetes capturados mostrando timestamp, IP origen, IP destino y protocolo (validado generando tráfico web real). La estación de trabajo L1 está completamente operativa para el análisis de tráfico y la implementación de reglas.
