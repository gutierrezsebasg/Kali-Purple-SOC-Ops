# Kali-Purple-SOC-Ops
# Módulo 1: Despliegue, Auditoría y Verificación del Entorno Defensivo [Completado]

## 1. Objetivo Práctico
Auditar la suite defensiva de Kali Purple, resolver dependencias faltantes y dejar la estación L1 operativa para inspección de tráfico.

## 2. Auditoría y Aprovisionamiento de Binarios Defensivos

**Comando inicial de verificación:**
```bash
which tshark tcpdump ufw
```
Al detectar herramientas faltantes y conflictos de firmas en los repositorios por defecto, procedemos con el aprovisionamiento manual

**Instalación de Firewall (Protect):**
```bash
sudo apt update
sudo apt install ufw -y
```
**Despliegue Forense Volatility 3 (Respond):**
```bash
git clone https://github.com/volatilityfoundation/volatility3.git
cd volatility3
python3 vol.py --help
```
| Herramienta | Categoría NIST | Estado | Uso SOC L1 |
| :--- | :--- | :--- | :--- |
| **Tshark** | Detect | Verificado | Inspección y filtrado de.pcap |
| **Tcpdump** | Detect | Verificado | Captura rápida en interfaces |
| **Volatility 3** | Respond | Clonado (GitHub) | Análisis forense de memoria RAM |
| **UFW** | Protect | Instalado | Contención por reglas de firewall |

## 3. Verificación de Captura en Vivo (Tshark)

**Prueba de monitoreo:**
```bash
sudo tshark -i any -c 10
```
Resultado:
Captura de 10 paquetes validada con tráfico web real. Se verificó timestamp, IP origen/destino y protocolo. Estación L1 operativa para análisis de tráfico.
