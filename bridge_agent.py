import os
import time
import requests
import subprocess

# Configuración: Tu URL de Vercel
API_URL = "https://asistente-ceo.losparceritos.com/api/comandos"

def ejecutar_comando_openclaw(instruccion):
    print(f"\n[CEO ORDER]: {instruccion}")
    print("🛠️ Ejecutando con OpenClaw...")
    try:
        # 1. Ejecutar la lógica de programación (Simulado o Real)
        # Nota: Asegúrate de tener openclaw instalado o cambia este comando por tu lógica
        subprocess.run(f"echo '{instruccion}' > ULTIMA_ORDEN.txt", shell=True) 
        
        print("✅ Archivo local generado.")
        
        # 2. Auto-Sincronización (Push automático a la web)
        print("🔄 Subiendo cambios a Vercel...")
        subprocess.run("git add .", shell=True)
        subprocess.run(f'git commit -m "Auto-build: {instruccion[:20]}"', shell=True)
        subprocess.run("git push origin main", shell=True)
        print("🚀 ¡Cambio en vivo en asistente-ceo.losparceritos.com!")
        return True
    except Exception as e:
        print(f"❌ Error de ejecución: {e}")
        return False

if __name__ == "__main__":
    print("📡 PUENTE ANTIGRAVITY SINCRONIZADO")
    print(f"🔗 Escuchando a: {API_URL}")
    print("Presiona Ctrl+C para detener.")

    while True:
        try:
            # Preguntar a la API si hay algo nuevo
            response = requests.get(API_URL)
            if response.status_code == 200:
                data = response.json()
                comando = data.get("comando")
                
                if comando:
                    ejecutar_comando_openclaw(comando)
                else:
                    # No hay órdenes, esperamos un poco
                    print(".", end="", flush=True) 
            else:
                print(f"\n⚠️ Error de conexión API: {response.status_code}")
            
            time.sleep(5) # Revisar cada 5 segundos
        except Exception as e:
            print(f"\n❌ Error en el loop: {e}")
            time.sleep(10)
        except KeyboardInterrupt:
            print("\n🛑 Puente cerrado por el CEO.")
            break
