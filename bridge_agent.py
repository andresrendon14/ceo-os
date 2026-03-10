import time
import requests
import os

# CONFIGURACIÓN DEFINITIVA - SISTEMA CEO-OS
# Agregamos el / al final para que Vercel no se confunda con las rutas
API_URL = "https://ceo-os-weld.vercel.app/api/"
CHECK_INTERVAL = 3  # Segundos entre revisiones

def ejecutar_comando(comando):
    """Procesador de órdenes en tu PC local"""
    print(f"\n🚀 ORDEN RECIBIDA DEL CEO: {comando}")
    
    try:
        # Lógica: Crear archivos en el escritorio (o carpeta actual)
        if "Crea el archivo" in comando or "archivo" in comando.lower():
            # Extraer el nombre del archivo de forma simple
            nombre = "orden_ceo_os.txt"
            if "archivo" in comando:
                partes = comando.split("archivo")
                nombre = partes[-1].strip().split(" ")[0].replace(".", "") + ".txt"
            
            with open(nombre, "w", encoding="utf-8") as f:
                f.write(f"--- SISTEMA CEO-OS ---\nEjecutado correctamente en PC local.\nOrden: {comando}\nFecha: {time.ctime()}")
            
            print(f"✅ ÉXITO: Archivo '{nombre}' generado físicamente.")
        
        else:
            print(f"⚠️ Comando detectado: '{comando}'. (Sin acción programada)")
            
    except Exception as e:
        print(f"❌ Error interno al ejecutar comando: {e}")

def iniciar_puente():
    print("------------------------------------------")
    print("📡 SISTEMA ANTIGRAVITY: PUENTE ACTIVO")
    print(f"🔗 Sincronizado con: {API_URL}")
    print("Estado: Esperando señal de Vercel...")
    print("Presiona Ctrl+C para apagar.")
    print("------------------------------------------")
    
    ultimo_id_comando = None
    
    while True:
        try:
            # Petición a la API de Vercel
            response = requests.get(API_URL, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                comando_actual = data.get("comando")
                
                # Solo ejecutar si hay un comando y es distinto al anterior
                if comando_actual and comando_actual != ultimo_id_comando:
                    ejecutar_comando(comando_actual)
                    ultimo_id_comando = comando_actual
                else:
                    # Puntitos para saber que el programa no está trabado
                    print(".", end="", flush=True)
            
            elif response.status_code == 404:
                print("\n🔍 Buscando señal... (Vercel está despertando la API)")
            else:
                print(f"\n❌ Error de API ({response.status_code}). Reintentando...")
                
        except requests.exceptions.RequestException:
            print("\n📶 Error de red: Revisando conexión...")
            time.sleep(5)
        except Exception as e:
            print(f"\n⚠️ Error imprevisto: {e}")
            
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    iniciar_puente()