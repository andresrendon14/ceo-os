import time
import requests
from datetime import datetime

# 🎯 EL ENLACE DE LA VICTORIA
API_URL = "https://ceo-os-parceritos.vercel.app/api"

def ejecutar_orden(cmd):
    hora = datetime.now().strftime('%H:%M:%S')
    print(f"\n[{hora}] ⚡ ORDEN MAESTRA EJECUTADA: {cmd}")
    try:
        with open("NUCLEO_CEO.txt", "w", encoding="utf-8") as f:
            f.write(f"SISTEMA OPENCLAW\nÚltima orden: {cmd}\nHora: {hora}")
    except Exception as e:
        pass

def iniciar_puente():
    print("="*55)
    print("🏆 SISTEMA OPENCLAW - ENLACE DEFINITIVO")
    print(f"🔗 Conectado a: {API_URL}")
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
            else:
                print(f"\n⚠️ Código {res.status_code}...")
        except:
            print("\n📶 Buscando señal...", end="")
        time.sleep(3)

if __name__ == '__main__':
    iniciar_puente()
