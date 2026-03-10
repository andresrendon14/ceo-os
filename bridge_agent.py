import os
import time
import requests
import subprocess

# Configuración
API_URL = "https://asistente-ceo.losparceritos.com/api/comandos"
LOCAL_PATH = os.path.dirname(os.path.abspath(__file__))

def ejecutar_comando_openclaw(instruccion):
    print(f"🛠️ Ejecutando instrucción de Andrés: {instruccion}")
    try:
        # Ejecutar OpenClaw
        subprocess.run(["openclaw", instruccion], shell=True)
        print("✅ Operación local completada.")
        
        # Sincronizar cambios a GitHub para que Vercel se actualice
        print("🔄 Sincronizando con la nube...")
        subprocess.run(["git", "add", "."], shell=True)
        subprocess.run(["git", "commit", "-m", f"Auto-build: {instruccion[:30]}"], shell=True)
        subprocess.run(["git", "push", "origin", "main"], shell=True)
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    print("📡 PUENTE ANTIGRAVITY ACTIVO")
    print("Esperando órdenes desde asistente-ceo.losparceritos.com...")
    
    # Por ahora, para la PRUEBA DE FUEGO, vamos a simular una espera activa
    # En la siguiente fase, este loop consultará tu API de Vercel
    while True:
        try:
            time.sleep(10)
        except KeyboardInterrupt:
            print("\n🛑 Puente cerrado por el CEO.")
            break
