import time
import requests
from datetime import datetime

# 🎯 LA CLAVE: URL de Producción pura (Libre del bloqueo de Preview)
API_URL = "https://ceo-os-weld.vercel.app/api"

def ejecutar_orden(cmd):
    hora = datetime.now().strftime('%H:%M:%S')
    print(f"\n[{hora}] ⚡ ORDEN MAESTRA EJECUTADA: {cmd}")
    try:
        with open("NUCLEO_CEO.txt", "w", encoding="utf-8") as f:
            f.write(f"SISTEMA OPENCLAW\nÚltima orden: {cmd}\nHora: {hora}")
    except Exception as e:
        print(f"Error local: {e}")

def iniciar_puente():
    print("="*55)
    print("🧠 SISTEMA OPENCLAW ACTIVADO - NIVEL DOCTORADO")
    print(f"🔗 Conectado a Producción Frontal: {API_URL}")
    print("="*55)
    
    ultimo = None
    while True:
        try:
            res = requests.get(API_URL, timeout=10)
            if res.status_code == 200:
                cmd = res.json().get("comando")
                if cmd and cmd != ultimo:
                    ejecutar_orden(cmd)
                    ultimo = cmd
                else:
                    print(".", end="", flush=True)
            elif res.status_code == 404:
                print("\n🔄 Esperando a que Vercel termine de compilar (404)...")
            else:
                print(f"\n⚠️ Ignorando ruido de red (Código {res.status_code})...")
        except:
            print("\n📶 Reconectando al servidor central...", end="")
        time.sleep(3)

if __name__ == '__main__':
    iniciar_puente()
