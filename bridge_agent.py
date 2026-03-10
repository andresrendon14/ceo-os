import time
import requests
import os

# CONFIGURACIÓN GLOBAL - SISTEMA CEO-OS
# Usamos la ruta raíz de la API para que Vercel la encuentre siempre
API_URL = "https://ceo-os-weld.vercel.app/api"
CHECK_INTERVAL = 3  # Revisar cada 3 segundos

def ejecutar_comando(comando):
    """Procesador de órdenes en tu PC local"""
    print(f"\n🚀 ORDEN RECIBIDA: {comando}")
    
    try:
        # Lógica para crear archivos (Prueba de concepto)
        if "Crea el archivo" in comando:
            # Extraer el nombre del archivo del comando
            partes = comando.split("archivo")
            nombre = "orden_ceo.txt"
            if len(partes) > 1:
                nombre = partes[1].strip().split(" ")[0]
                if not nombre.endswith(".txt"):
                    nombre += ".txt"
            
            with open(nombre, "w", encoding="utf-8") as f:
                f.write(f"Ejecutado por CEO-OS\nComando: {comando}\nFecha: {time.ctime()}")
            print(f"✅ ÉXITO: Archivo '{nombre}' generado en la carpeta local.")
        
        else:
            print(f"⚠️ Comando detectado pero sin acción programada: {comando}")
            
    except Exception as e:
        print(f"❌ Error al ejecutar: {e}")

def iniciar_puente():
    print("------------------------------------------")
    print("📡 SISTEMA ANTIGRAVITY: PUENTE ACTIVO")
    print(f"🔗 Sincronizado con: {API_URL}")
    print("Presiona Ctrl+C para apagar el sistema.")
    print("------------------------------------------")
    
    ultimo_comando = None
    
    while True:
        try:
            # Petición a la nube
            response = requests.get(API_URL, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                comando_actual = data.get("comando")
                
                # Solo actuar si hay un comando nuevo
                if comando_actual and comando_actual != ultimo_comando:
                    ejecutar_comando(comando_actual)
                    ultimo_comando = comando_actual
                else:
                    # Indicador visual de que el puente sigue vivo
                    print(".", end="", flush=True)
            
            elif response.status_code == 404:
                print("\n🔍 Buscando señal... (Error 404: Vercel aún no activa la API)")
            else:
                print(f"\n❌ Estado de API inesperado: {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            print("\n📶 Error de conexión: Reintentando en 5 segundos...")
            time.sleep(2)
        except Exception as e:
            print(f"\n⚠️ Error imprevisto: {e}")
            
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    iniciar_puente()